from seleniumbase import SB

def main():
    
    # My proxy
    proxy = "username:password@proxy_host:proxy_port"

    with SB(uc=True, headless=True, proxy=proxy) as sb:
        sb.driver.uc_open_with_reconnect("https://www.digezz.ch", reconnect_time=10)
        
        print(sb.driver.title)
        print(sb.driver.page_source)
    
if __name__ == "__main__":
    main()
