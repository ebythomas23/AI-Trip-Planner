import os 
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv


class PlaceSearchTool:
    def __init__(self):
        self.google_api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_places_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self.__setup_tools()

    def __setup_tools(self)-> List:
        """ Setup all tools for the place search tool"""


        @tool
        def search_attractions(place:str)-> str:
            """Search attractions of a place"""
            try:
                attraction_result= self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} suggested by google: {attraction_result}"
                
            except Exception as e:
                tavily_result = self.tavily_places_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \n Following are the attractions of {place}: {tavily_result}"


        @tool
        def search_restaurants(place:str)->dict:
            """ search restaurants of a place """
            try:
                restaurant_result = self.google_places_search.google_search_restaurants(place)
                if restaurant_result:
                    return f"Following are the restaurants of {place} suggested by google: {restaurant_result}"
    
            except Exception as e:
                tavily_result = self.tavily_places_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \n Following are the restaurants of {place}: {tavily_result}"

        @tool
        def search_activities(place:str)->dict:
            """Search activities of a place"""
            try:
                activity_result = self.google_places_search.google_search_activity(place)
                if activity_result:
                    return f"Following are the activites in and around {place} suggested by google: {activity_result}"
                
            except Exception as e:
                tavily_result = self.tavily_places_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \n Following are the activities of {place}: {tavily_result}"

        @tool
        def search_transportations(place:str)->dict:
            """Search transportation of a place"""
            try:
                transport_result = self.google_places_search.google_search_transportation(place)
                if transport_result:
                    return f"Following are the transportations in {place} suggested by google: {transport_result}"
                

            except Exception as e:
                tavily_result = self.tavily_places_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \n Following are the transportations of {place}: {tavily_result}"


        return [search_activities,search_attractions,search_restaurants,search_transportations]