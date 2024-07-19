gdp = {"Canada":150, "USA":350, "China":1350, "France":75} # dict

with open('visual.html', 'w') as file:
    file.write('''  <style>
                        div {
                            background-color: green;
                            border-radius: 50%;
                            display: inline-block;
                            text-align: center;
                        }

                    </style>
                ''')

    for country, amount in gdp.items():
        file.write(f'<div style="height:{amount}px;width:{amount}px;">{country}</div>\n')
