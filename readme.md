# Level 1

- Requests Library

# Level 2

- Requests Library
- BeautifulSoup

# Level 3

- Requests Library
- BeautifulSoup
- Seleniumbase

## Level 31

- Sophisticated Digezz-Scraper with Seleniumbase

# Level 4

- Chromedriver Simple Example in a Headless Environment (same as Level 3 but with Parameter `headless = True`)

## Additional Configuration

To run Seleniumbase with Chrome on a Linux machine in a headless environment, additional configuration is necessary.

### Install Google Chrome

First, ensure your system packages are up to date:

```
sudo apt update
sudo apt upgrade -y
```

Install necessary dependencies for Chrome and Selenium:

```
sudo apt install -y wget unzip xvfb libxi6 libgconf-2-4
```

Download the latest stable version of Google Chrome:

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

Install the downloaded package:

```
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

If you encounter dependency issues, run:

```
sudo apt install -f -y
```

Check that Chrome is installed correctly:

```
google-chrome --version
```

You should see an output like Google Chrome 117.0.5938.62.

### Enable RAM Swap

If you're running on a Droplet with limited RAM ( < 1GB ) Chrome will likely run out of memory and crash when scraping. To avoid this, enable RAM Swap. This means that a part of the SSD will be used for RAM.

First, verify if any swap space is currently enabled:

```
sudo swapon --show
```

If there's no output, it means no swap space is active.

Create a Swap File

Decide on the size of the swap file. A common practice is to set swap space equal to or double the amount of RAM, depending on your needs and available disk space. Here, we’ll create a 2GB swap file.

```
sudo fallocate -l 2G /swapfile
-l 2G: Allocates 2 gigabytes.
file.
```

/swapfile: The location of the swap

Secure the Swap File

Set the correct permissions to prevent unauthorized access:

```
sudo chmod 600 /swapfile
```

Mark the File as Swap Space

Format the file to swap:

```
sudo mkswap /swapfile
```

You should see output confirming the swap space:

```
Setting up swapspace version 1, size = 2 GiB (2147479552 bytes)
no label, UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Activate the swap file:

```
sudo swapon /swapfile
```

Verify Swap Activation

Confirm that the swap is active:

```
sudo swapon --show
```

You should see:

```
NAME TYPE SIZE USED PRIO
/swapfile file 2G 0B -2
```

Also, check with free -h:

```
free -h
```

The "Swap" row should now display the total and free swap space.

To ensure the swap file is used after a reboot, add it to /etc/fstab:

```
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

If this doesnt work, ask ChatGPT for help.

## Level 41

- Seleniumbase with Chrome in a Headless Environment
- With Proxys enabled

For this to work:

- Purchase an ISP Proxy from [IPRoyal](https://iproyal.com/)
