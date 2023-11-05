ascii_code_1 = '''

██████╗ ██╗   ██╗███╗   ███╗ █████╗ ███████╗██╗  ██╗
██╔══██╗╚██╗ ██╔╝████╗ ████║██╔══██╗██╔════╝██║ ██╔╝
██████╔╝ ╚████╔╝ ██╔████╔██║███████║███████╗█████╔╝ 
██╔═══╝   ╚██╔╝  ██║╚██╔╝██║██╔══██║╚════██║██╔═██╗ 
██║        ██║   ██║ ╚═╝ ██║██║  ██║███████║██║  ██╗
╚═╝        ╚═╝   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

'''

print(ascii_code_1)
print('by Xicopz')
original_link = input('Paste the link you would like to mask (without http or https): ')
fake_domain = input('''Enter the domain you would like you site to appear as (with http or https)
 eg: https://instagram.com: ''')
social_enginnering = input('''Enter social enginnering words. eg: free-robux''')
masked_link = fake_domain + '-' + social_enginnering + '@' + original_link
print('Here is your masked link: ' + masked_link)