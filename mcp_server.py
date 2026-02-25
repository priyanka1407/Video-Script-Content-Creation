from mcp.server.fastmcp import FastMCP
from app import get_realtime_info, generate_video_script

mcp =FastMCP("This is for video content creation. It should generate summaries and video scripts based on the provided information.")

@mcp.tool()
async def get_latest_info_mcp(query):
    return get_realtime_info(query)

@mcp.tool()
async def get_video_script_mcp(query):
    info_text = get_realtime_info(query)
    return generate_video_script(info_text)


if __name__ == "__main__":
    mcp.run(transport="stdio")
