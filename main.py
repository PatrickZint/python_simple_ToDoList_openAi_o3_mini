from LLMReasoner import LLMReasoner
from GitHubManager import GitHubManager
import os

from agents.goal_analysis_agent import GoalAnalysisAgent
from agents.environment_analysis_agent import EnvironmentAnalysisAgent
from agents.spec_gen_agent import SpecificationGenerationAgent
from agents.architecture_design_agent import ArchitectureDesignAgent
from agents.code_gen_agent import CodeGenerationAgent

def main():
    # Initialize components
    llm_reasoner = LLMReasoner()
    # Initialize GitHub manager with a personal access token and repository name
    # These are from the newly created GitHub repository that will be used to store the generated code
    github_manager = GitHubManager(os.getenv('GITHUB_TOKEN'), 'repository_name')



    # Agent Pipeline
    goal_agent = GoalAnalysisAgent(llm_reasoner, github_manager)
    refined_goals = goal_agent.process_goals('inputs/goals.txt')
    print("Refined Goals:", refined_goals)

    env_agent = EnvironmentAnalysisAgent(llm_reasoner, github_manager)
    env_profile = env_agent.analyze_environment('inputs/environment.txt')
    print("Environment Profile:", env_profile)

    # Generate System Specifications
    spec_gen_agent = SpecificationGenerationAgent(llm_reasoner, github_manager)
    specifications = spec_gen_agent.generate_specifications('outputs/refined_goals.txt',
                                                            'outputs/refined_environment.txt')
    print("System Specifications:", specifications)

    # Design System Architecture
    arch_design_agent = ArchitectureDesignAgent(llm_reasoner, github_manager)
    architecture_design = arch_design_agent.design_architecture('outputs/system_specifications.txt')
    print("System Architecture Design:", architecture_design)

    # Generate Codebase
    code_gen_agent = CodeGenerationAgent(llm_reasoner, github_manager)
    codebase = code_gen_agent.generate_codebase('outputs/system_architecture.txt', 'outputs/system_specifications.txt')
    print("Generated Codebase:", codebase)

if __name__ == "__main__":
    main()