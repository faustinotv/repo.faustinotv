# -*- coding: utf-8 -*-
#                 -*- adritecNews -*-                      #
#----------------------------------------------------------#
#  INSTALADOR DE ADD-ONS PARA O KODI XBMC - VERSÃO: 2.2.3  #
#----------------------------------------------------------#
# KODI: GPL https://pt.wikipedia.org/wiki/Kodi             #   
# KODI WIKI: https://kodi.wiki/view/Main_Page              #
# PROGRAMAÇÃO: PYTHON: https://docs.python.org/2/tutorial/ #
# CONTATO: adritec_dados@yahooo.com.br                     #
# CANAL: http://YouTube.com/adritecnews                    # 
# SITE: http://adritecnews.com                             #
#----------------------------------------------------------#
#     TODOS OS DIREITOS RESERVADOS: adritecNews 2018       #
#                                                          #
#      Este trabalho está licenciado sob uma Licença       #
#Creative Commons Atribuição-NãoComercial-SemDerivações 4.0# 
#      Internacional. Para ver uma cópia desta licença,    # 
# visite http://creativecommons.org/licenses/by-nc-nd/4.0/ #
#       'Atribuição-Não-Comercial-SemDerivativos 4.0       # 
#             Internacional (CC BY-NC-ND 4.0)'             #
#----------------------------------------------------------#
#                "ATENÇÃO INTERNAUTAS"                     #
#                                                          #
#       FICA PROIBIDO CÓPIA, MODIFICAÇÃO, DIVULGAÇÃO       #
#                SEM MINHA ALTORIZAÇÃO                     #
#    Add-on desenvolvido para fazer AJUSTES no seu KODI,   #
#   para Inscritos e não inscritos do canal adritec News.  #
#----------------------------------------------------------#
import zlib
import base64
def decode_base64( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)
def base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )
	
exec(decode_base64('xVbNbuM2ED5bTzEIEFBCXNortChgwC3ycwmwP0W3hwKBYdASJXNDkSpJ7SY59VnaQ9Fn6K15kz5Jh9Sv07jY3UNrQBY5Px+HMx+HElWtjYO7XZXNwz/Lc63aYdmIdlDLphQo1HYO9t62wvcFDkqpd5FoMey+cUL2s8ZIKXbpvH33UsP7kRMVjwqjK5RZ3ZiMW4qGNGe5ttAZVUw1jquM6Sg694FdX8GatOHQ2ujSsIqy3AjHM8U/WKGsY1KGPVgS1Sy7ZSW3uTCAvzWEwKkzTFnJHP+OuX2sLa3xTd9poWJia54JJleLxV5XfNEiLXogMickSSK3b6qdYkLa47BPkRrLTc4cW/wwOJMkytFClwjR5ZteBUGcRJY7J1SvCnHQkII4oSV3b1t1JDKtfPid3WfsjcAZdLmdEw+X0lqVfpuRKKALIyascTqTnCmSwHoNxJmGk1U0A/RwRkvqleaSZXuO0c8ipZ0o7reVzjnGNsBMxLh9D7oNqDA1wiIa19Q082hoVgjJrXjwQEK5eLDr5VsmuXE+5EESSnTMPihHp4rddQXePojaPvXqdAp9uLGjW+Q0km3rAVP0WU7mYZrpRrkwigptAEnoazH3A8UqjqfHxxOGuCAeLvqBydt4QtoE8zuizDxK4U0HP9R3BmdreIGTokbTg6oPyxZYldkkxLPREPnkRXFRJ5NNOH7nFz45pcviBE4hHlWLF8v0y+VySZe+1KIICTv0TOAb6PPtt7HXIgt5esp0es+t0vHJzeWbl2++B5DYGDY3F5u/fv7lZnGxuVkE+aZVrw3PN+fIGniJLYI/sF59MgdyiUx8/L0CZn5qxHvsIopBzZBMK+jAvbfnu3XmH+GeEXh1AT0efPGcT8g1mgIZ7JAx7T4JRnDFLX/HgNWsZAbXNgwcN9jGhAVua/b4m/7W2134qPzJKYSpmKEUhZgGyXZcrslbUZG50t3s9eOvGs/ADLM8JBGL7Us/tkdaN6bEM99Sxx/A2WzKunSkXTrhXTol3tjVPO8C2dIDtqWrwLD0CMU8cHpIsvR5lqVPaZYe4Vk6JdrzPEunRGuP/X9MN1H57vBJbEsDhzzfYGDc/8ufnEuMbLybAoU+vRl8RllD/zi4LYbbpb3S+B3PMMxdI6Tz19iPF68u6WvvIDLmBN6Ip9hLxychfjXyUQWGUsvca68VEr7CBGO2pmaYWOihcs5re3u/k00A/POPqSGg5LxrPF6+AnKkz0CoPPGvjwW+binW4f47pQggQb7G5GLo/deB/2bBNFArcaX4q8Sn/ODuHVM+4cT0Rv8b'))