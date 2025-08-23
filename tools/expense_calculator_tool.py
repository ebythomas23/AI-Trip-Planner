from utils.expense_calculator import Calculator
from langchain.tools import tool
from typing import List

class CalculatorTool():
    def __init__(self) -> None:
        self.calculator = Calculator()
        self.calculator_tool_list = self.__setup_tools()


    def __setup_tools(self)-> List:
        """Setup tools for the calculator tool"""

        @tool
        def estimate_total_hotel_cost(price_per_nigt:str,total_days:float)->float:
            """Calculate Total Hotel Cost"""
            return calculator.multiply(price_per_nigt,total_days)
        

        @tool
        def calculate_total_cost(*costs:float)->float:
            """ Calculate ToTAL Expense of the  trip"""
            return calculator.calculate_total(*costs)
        
        @tool
        def calculate_daily_expense_budget(total_cost :float , days:int)->float:
            """Calculate daily budget"""
            return self.calculator.calculate_daily_budget(total_cost, days)
        
        return[estimate_total_hotel_cost, calculate_total_cost, calculate_daily_expense_budget]