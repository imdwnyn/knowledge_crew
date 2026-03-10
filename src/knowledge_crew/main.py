from knowledge_crew.crew import KnowledgeCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'query': 'What is scoring function and what are the different scoring functions used in the paper.'
    }

    try:
        KnowledgeCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")