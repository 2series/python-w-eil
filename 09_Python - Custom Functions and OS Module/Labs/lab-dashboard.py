# import os
# from time import sleep

# site = ['cnn.com', 'fox.com', 'tacobell.com', 'notarealsite.tv', 'w3schools.com', 'sabcsport.com']
# header = '<meta http-equiv="refresh" content="5">'

# def status(site):
#     color = 'red'
#     command = f'ping -c 1 {site}'
#     response = os.popen(command).read()

#     if '1 packets received' in response:
#         color = 'green'

#     return response, color

# while True:
#     os.system('clear')
#     page = header
#     for item in site:
#         result = status(item)
#         page = f''' 
#                     {page}
#                     <h2 style="background-color:{result[1]};">{item}</h2>
#                     <pre>{result[0]}</pre>
#                 '''

#     try:
#         with open('dashboard.html', 'w') as file:
#             file.write(page)
#     except:
#         print('ERROR - Writing to File')

#     sleep(1)



import os
from time import sleep

site = ['cnn.com', 'fox.com', 'tacobell.com', 'notarealsite.tv', 'w3schools.com', 'sabcsport.com']
header = '<meta http-equiv="refresh" content="5">'

def status(site):
    """
    Check the status of a website by pinging it.

    Args:
        site (str): The website to check.

    Returns:
        tuple: A tuple containing the ping response and a color indicator (green if the site is up, red if it's down).

    Example:
        >>> status('google.com')
        ('64 bytes from lb-in-f188.1e100.net (216.58.194.174): icmp_seq=1 ttl=57 time=26.8 ms\\n', 'green')
    """
    color = 'red'
    command = f'ping -c 1 {site}'
    response = os.popen(command).read()

    if '1 packets received' in response:
        color = 'green'

    return response, color

def generate_dashboard(sites, header):
    """
    Generate an HTML dashboard that displays the status of multiple websites.

    Args:
        sites (list[str]): A list of websites to check.
        header (str): The HTML header for the dashboard.

    Returns:
        str: The generated HTML dashboard.

    Example:
        >>> sites = ['cnn.com', 'fox.com']
        >>> header = '<meta http-equiv="refresh" content="5">'
        >>> print(generate_dashboard(sites, header))
        <html content>
    """
    page = header
    for site in sites:
        result = status(site)
        page = f''' 
                    {page}
                    <h2 style="background-color:{result[1]};">{site}</h2>
                    <pre>{result[0]}</pre>
                '''
    return page

def main():
    """
    Main function that generates and updates the HTML dashboard.

    Example:
        >>> main()
        (runs indefinitely, updating the dashboard every second)
    """
    while True:
        os.system('clear')
        page = generate_dashboard(site, header)
        try:
            with open('dashboard.html', 'w') as file:
                file.write(page)
        except:
            print('ERROR - Writing to File')
        sleep(1)

if __name__ == '__main__':
    main()