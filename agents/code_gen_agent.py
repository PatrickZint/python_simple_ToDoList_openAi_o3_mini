class CodeGenerationAgent:
    def __init__(self, llm_reasoner, github_manager):
        self.llm = llm_reasoner
        self.github = github_manager

    def generate_codebase(self, architecture_file, specifications_file):
        # Read system architecture and specifications from GitHub
        architecture = self.github.read_file(architecture_file)
        specifications = self.github.read_file(specifications_file)

        # Generate codebase
        prompt = (
           f"You are a software engineer. Based on the following system architecture and specifications, "
           f"generate the full codebase including front-end code, back-end code, and database models.\n\n"
           f"System Architecture:\n{architecture}\n\n"
           f"System Specifications:\n{specifications}"
        )

        codebase = self.llm.get_chat_response(prompt)

        # Save codebase
        file_path = 'outputs/generated_codebase.zip'
        commit_message = "Generated Codebase"
        
        try:
            # Check if the file exists
            existing_file = self.github.get_contents(file_path)
            self.github.update_file(file_path, commit_message, codebase, existing_file.sha)
        except self.github.GithubException as e:
            if e.status == 404:
                # File does not exist, create it
                self.github.create_file(file_path, commit_message, codebase)
            else:
                raise e

        return codebase