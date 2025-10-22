import sys
import os
import asyncio

from dotenv import load_dotenv
load_dotenv()
sys.path.append(os.path.abspath("../src"))

from IPython.display import Image, display
from deep_research_from_scratch.research_agent_mcp import agent_mcp

async def main():
    # Show the agent
    display(Image(agent_mcp.get_graph(xray=True).draw_mermaid_png()))
    
    # Run the agent
    from utils import format_messages
    from langchain_core.messages import HumanMessage
    
    research_brief = """I want to identify and evaluate the coffee shops in San Francisco that are considered the best based specifically  
    on coffee quality. My research should focus on analyzing and comparing coffee shops within the San Francisco area, 
    using coffee quality as the primary criterion. I am open regarding methods of assessing coffee quality (e.g.,      
    expert reviews, customer ratings, specialty coffee certifications), and there are no constraints on ambiance,      
    location, wifi, or food options unless they directly impact perceived coffee quality. Please prioritize primary    
    sources such as the official websites of coffee shops, reputable third-party coffee review organizations (like     
    Coffee Review or Specialty Coffee Association), and prominent review aggregators like Google or Yelp where direct  
    customer feedback about coffee quality can be found. The study should result in a well-supported list or ranking of
    the top coffee shops in San Francisco, emphasizing their coffee quality according to the latest available data as  
    of July 2025."""
    
    result = await agent_mcp.ainvoke({"researcher_messages": [HumanMessage(content=f"{research_brief}.")]})
    format_messages(result['researcher_messages'])

if __name__ == "__main__":
    asyncio.run(main())
    
    

