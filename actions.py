from SimplerLLM.tools.rapid_api import RapidAPIClient

def get_seo_page_report(url: str):
    """
    Calls the RapidAPI endpoint to get a basic SEO audit for the provided URL.
    """
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {'url': url}
    
    api_client = RapidAPIClient()
    try:
        response = api_client.call_api(api_url, method='GET', params=api_params)
        return response  # Return the JSON response directly
    except Exception as e:
        return {"error": str(e)}  # Handle errors gracefully
