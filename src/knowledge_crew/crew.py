from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
# from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from crewai_tools import PDFSearchTool
from typing import List

# research_paper_source = PDFKnowledgeSource(
#     file_paths=["survey_on_icl.pdf"],
#     chunk_size=1500,
#     chunk_overlap=250
# )

@CrewBase
class KnowledgeCrew():
    """KnowledgeCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def research_summarization(self) -> Agent:
        return Agent(
            config=self.agents_config['research_summarization'],
            tools=[PDFSearchTool(pdf="knowledge/survey_on_icl.pdf")],
            verbose=True
        )

    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['summarization_task'],
            output_file="report.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the KnowledgeCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # knowledge_sources=[research_paper_source]
            # must uv add numpy and qdrant_client
        )
