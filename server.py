from fastmcp import FastMCP
from expense_tracker import register_expense_tools as expense_tools
from dice import register_dice_tools as dice_tools

mcp = FastMCP(name="unified_server")
expense_tools(mcp)
dice_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
