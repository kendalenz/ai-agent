from SimplerLLM.tools.rapid_api import RapidAPIClient

def get_seo_page_report(url: str):
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {'url': url}
    api_client = RapidAPIClient()

    try:
        response = api_client.call_api(api_url, method='GET', params=api_params)
        print(f"API Response for {url}: {response}")  # Log the API response
        return response
    except Exception as e:
        print(f"Error fetching SEO report for {url}: {e}")
        return {"error": str(e)}

