#!/usr/bin/python
# -*- coding: utf-8 -*-
#                 -*- adritecNews -*-                      #
#----------------------------------------------------------#
#  INSTALADOR DE ADD-ONS PARA O KODI XBMC - VERSÃO: 2.0.0  #
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
exec(decode_base64('ZZDBbsMgDIbP5SlQL22liEq759Cul0pTU027RTmQmCBLBEdAtG5PvwTCOmkczM/vzzaAw0gu8Ec7dEWMEoBsknrCJEYzabQF+cJ/eYapZHLGYPtSpD27TmUVcPjV3zj2aBTrHQ0z4mlynfJirhMggTxfuY5scGQSBzKopUlO5jNjMPLnKvNdxQWlIX13pOcRfn9gEA2+2fyD5mR86NX29GwSLXFa4v4gtAqnzDAW5QcGo8pt/Vq9Ve8cCLRyrZlUU58bCQ6D6urjuamPEWhWzilYgJv69EuWr7YmE/3q9rdmmyZdL7zcpX8X4/IiOYh1gp37oPVBGhMv7Hc/'))	
exec(decode_base64('1VbdbiI3FL4enuJ0pNXMdGFItqu2iwISJEM1SoAVsGnViCIz9gRvhjGyPSHpa/QRelH1uurNXjYv1uNhhgAhu+3eVEVCYPs7Pz7fd2xTFsPdIplSosmU0NsR05qn12oqEuoq/jPzGhWrBDRt266cfFGrwekwbJ8N4O1gCO2zYTgOTqEffD+CWq11gl5IGjGqCletigVwkjK9EvImH+AwymQSJZyliFkwkenW8dFJ/ensFjwRK7VkjJql1qsCvTO5BZZMS85U69UaVg7NesWyTiISzdmCLWZZHDNp9tl6oRD6dDqHr8cLQZlxuDUyi5IRup6KSaSFzHN7MpkXob6pwkn9SZmwuPACTNCKhflmMt0wU7Eq9Dmi+mz1eURVDjC1TdS/5OkpR8cHOfpHFO3UyuANMSYIkiPk/YawrSES9TGecpoKLl77BUMlNyZcEeIAMZ+u5Meoy5lbSa7ZtH12OR0F43HY/240/aF34cY8Qd6KHQPwGFKhQSh/SfTcZ3dcaeUaT2tgDjKfFddzEEuWbharYK9sD4iC+BFmPrGfx3bLfLx1QuUmSxm5Rj6Y0rQbXgRo1gS4my0iX0uSqoRo9hYzcsvM3gueug6SGnGSNOr1uViweqaYNBEcqIKzX0Qf4zueV7F6Qa9MrYxxzXSYxuKCzFji2qN7pdnC7+XMulpokng2GnaHQVAYf9SwKxlbGxurzrtuNxhOu2sryXyVzVzn6qej2puJU3WcauF2H8pT7ZYTHtThK6sEjMIfAwRs0F/C8dGr18VPxdLyvgHng7PwcmubcSKIdp/PuZPxhF6aE0ektnfVeD3BfNhdxJa6dNaE46/xtKlY0VzwiOGYYu3FtX/PVCpwS6eDC5QmFfSayVmSsclVZ0Ko4T66qncmV/UcMClwklEDwMNDmVUopq/x2Dfzg/4Bm9UcnU2gBuU87AGie5JOgouwF/bbQxgP25ftXtAfD0YlzkFloHes98Mv2E5wEV4OA9Q8KJbBuaDcRG2AAy9BaemW3EDV6RCF/SogJaAyAtj3D39ITiDht0gqmJRzJ+ueh4ffdz09UvkS53odpD5QkUjmBLIFwVZ6+O3hVwFkRvid8H3fqaYiMRQ1y8ImeHhN2suER0RC+9148LgnZOAA9jIYht3wtD3cAJFT7PCSvyYcNczl8tjLZfvt9LJlGaO1Bloogm8am6MFNfD8jbDZtNGraTzLYolin7bOL/4D1ub79DDByUKH4sZtUyrSMdd4HBmax2RB0rlATZa04MnDU47jSCzEIYbycFVnT41vhYSY3ApZRd2ig4gzELleYEkkAVLQghWLRBrz60wSJPRPpnx/W8em4TFlbK1kh4hjU+ad7p5im05v2P1MEEldkzfJEt3cTxTmKEqsWtPebatBZ/Rs/zT2u2a3ZQMUD09xM8JVHjx8SPDWzP/2//pgfkjEUbCUwYEAZb3eFOBtiG9Ow/+N2D5baJ210GLBN2L7z3RmrV9tptzTnXt2Z8aUBi8GYrbk5xtzOW3mf8IzzzfYR+PiIfiMPG17S5HmP6eUpc0uQS6geD6UVkVY/3zfy8ZFaQ/ejqFPRU9Qkrhe+WZxH9e4OjWFkQtGXQ+2XizFqyjDouJ7bMsCdzJmd9rFZrIzHde+tYt4hUWRFRbzbw=='))