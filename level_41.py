from seleniumbase import SB

def main():
    
    # My proxy
    proxy = "username:password@proxy_host:proxy_port"

    with SB(uc=True, headless=True, proxy=proxy) as sb:
        sb.driver.uc_open_with_reconnect("https://www.coop.ch/de/weine/alle-weine/c/m_2508?q=%3Arelevance&sort=relevance&pageSize=60&page=1#1000666018", reconnect_time=10)
        
        print(sb.driver.title)
        print(sb.driver.page_source)
    
if __name__ == "__main__":
    main()
