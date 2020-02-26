#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoded by pyprotect
# http://gabrielsilva.tk/pyprotect
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
import base64, codecs
magic = 'IyEvdXNyL2Jpbi9weXRob24NCiMgLSotIGNvZGluZzogdXRmLTggLSotDQojICAgICAgICAgICAgICAgICAtKi0gYWRyaXRlY05ld3MgLSotICAgICAgICAgICAgICAgICAgICAgICMNCiMtLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tIw0KIyAgSU5TVEFMQURPUiBERSBBREQtT05TIFBBUkEgTyBLT0RJIFhCTUMgLSBWRVJTw4NPOiAyLjIuMyAgIw0KIy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0jDQojIEtPREk6IEdQTCBodHRwczovL3B0Lndpa2lwZWRpYS5vcmcvd2lraS9Lb2RpICAgICAgICAgICAgICMgICANCiMgS09ESSBXSUtJOiBodHRwczovL2tvZGkud2lraS92aWV3L01haW5fUGFnZSAgICAgICAgICAgICAgIw0KIyBQUk9HUkFNQcOHw4NPOiBQWVRIT046IGh0dHBzOi8vZG9jcy5weXRob24ub3JnLzIvdHV0b3JpYWwvICMNCiMgQ09OVEFUTzogYWRyaXRlY19kYWRvc0B5YWhvb28uY29tLmJyICAgICAgICAgICAgICAgICAgICAgIw0KIyBDQU5BTDogaHR0cDovL1lvdVR1YmUuY29tL2Fkcml0ZWNuZXdzICAgICAgICAgICAgICAgICAgICAjIA0KIyBTSVRFOiBodHRwOi8vYWRyaXRlY25ld3MuY29tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAjDQojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSMNCiMgICAgIFRPRE9TIE9TIERJUkVJVE9TIFJFU0VSVkFET1M6IGFkcml0ZWNOZXdzIDIwMTggICAgICAgIw0KIyAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC'
love = 'NtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNwQDbwVPNtVPNtEKA0MFO0pzSvLJkbolOyp3GQbFOfnJAyozAcLJEiVUAiLvO1oJRtGTywMJ7Qc2RtVPNtVPNtVj0XV0AlMJS0nKMyVRAioJ1ioaZtDKElnJW1npBaj6AiYH7Qb29Qo21ypzAcLJjgH2IgETIlnKMuj6sQgJImVQDhZPZtQDbwVPNtVPNtFJ50MKWhLJAco25uoP4tHTSlLFO2MKVtqJ1uVTCQf3OcLFOxMKA0LFOfnJAyofBaLFjtVPNtVlNAPvZtqzymnKEyVTu0qUN6Yl9wpzIuqTy2MJAioJ1ioaZho3WaY2kcL2Ihp2ImY2W5YJ5wYJ5xYmDhZP8tVj0XVlNtVPNtVPNaDKElnJW1npBaj6AiYH7Qb28gD29gMKWwnJSfYIAyoHEypzy2LKEcqz9mVQDhZPNtVPNtVPNwVN0XVlNtVPNtVPNtVPNtVPOWoaEypz5uL2yiozSfVPuQDlOPJF1BDl1BEPN0YwNcWlNtVPNtVPNtVPNtVPNwQDbwYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYF0gYFZAPvZtVPNtVPNtVPNtVPNtVPNtVxSHEH7Qu8BQGlOWGyESHx5OIIEOHlVtVPNtVPNtVPNtVPNtVPNtVPNtVPNwQDbwVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPZAPvZtVPNtVPNtExyQDFODHx9WDxyRGlOQj5ADFHRfVR1CERyTFHAOj4sQt08fVREWIyIZE0UQu8BQGlNtVPNtVPNwQDbwVPNtVPNtVPNtVPNtVPNtVSASGFOAFH5VDFOOGSECHxynDpBUj4ACVPNtVPNtVPNtVPNtVPNtVPNtVPNtVj0XVlNtVPOOMTDgo24tMTImMJ52o2k2nJEiVUOupzRtMzS6MKVtDHcIH1ESHlOholOmMKHtF09RFFjtVPNwQDbwVPNtpTSlLFOWoaAwpzy0o3ZtMFOhj6AiVTyhp2AlnKEi'
god = 'cyBkbyBjYW5hbCBhZHJpdGVjIE5ld3MuICAjDQojLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSMNCmltcG9ydCB6bGliDQppbXBvcnQgYmFzZTY0DQpkZWYgZGVjb2RlX2Jhc2U2NCggYjY0c3RyaW5nICk6DQogICAgZGVjb2RlZF9kYXRhID0gYmFzZTY0LmI2NGRlY29kZSggYjY0c3RyaW5nICkNCiAgICByZXR1cm4gemxpYi5kZWNvbXByZXNzKCBkZWNvZGVkX2RhdGEgLCAtMTUpDQoNCmRlZiBiYXNlNjRfZW5jb2RlKCBzdHJpbmdfdmFsICk6DQogICAgemxpYmJlZF9zdHIgPSB6bGliLmNvbXByZXNzKCBzdHJpbmdfdmFsICkNCiAgICBjb21wcmVzc2VkX3N0cmluZyA9IHpsaWJiZWRfc3RyWzI6LTRdDQogICAgcmV0dXJuIGJhc2U2NC5iNjRlbmNvZGUoIGNvbXByZXNzZWRfc3RyaW5nICkNCgkNCmV4ZWMoZGVjb2RlX2Jhc2U2NCgnZlZUYmJ1TTJFSDIydm1KZ1lHR3BWV1habTgwV0xsTEFUbmEzUVM1ZXBObnRBb0ZoU09MWUlVS0pBa25sOWp0OTZFTS9vVys3UDlhaEpGdVNjeUVnYWpoejVuQTRIQTVQYzZrTTNNZHA0cGR6eEpqTUtuRmQ4RXJJUmJIbW1TKzFyeCswd3l1WFFnbkI0N0ZmL1RkYWhSdko4SFFyUC9KOHhRVTZLeVZUWUpGQmE0VGF1Rms3RHN1aEdRZWJHSUlqSGdtNS9xemtXcUhXcnVld1VnRzkzaE1RR2NzREhHY3IyWkNVcW1CcVo5Y0wxbWltRzR6amxPSWxOd0pIaE81ZkhjNVA1eGZBSkZ1amlrV0JpNnZaSW1LS0cweXVoclBGMWJBRUxHcWNRbVlCNTNpbnJSVnE5VnFLVWo4L2Y4Ym43cHJJRnBPTkZqcHFjckp4cVRUNjhjK1B2MlhidlYvRmVud0VCNFBxUm9MYzVpUktnenJBak1MZ21UYV'
destiny = 'WSG1qFBJAPrRIbEaORIJ1bnyI5JaMAqHIdFzuvZ1Mhq01wpIAbrGuLpUcZFREXIGAwI3cYLzkTpRkdGxg4qHWAHT5YnHqlARkEoxZinyIuY3qGoyOcoaH0YmAJY3IvY253ISEDDzL2EwuEnmA3Z2E2Z3qynxIvM25zZKyyozMiMlgOZ0AXZUu1pRSyFQRmIUECDaxiETAXM05VAP9QqzVmAR05o0MGoTIyqmWwoaABq0WyZmEzE0AiETZjAIWLFKIAAacRAUy2FHcPIx5LnGA0F0ASqxMeqHEQnRgTIxq0qGL4pwyzqQuzq01OFT1co293JKWwoUSELyMapRgjrxcZImMOFTEapaAJGyO1Jx5IGRMPpxL4HzWvDauPHxqlGHymqTyVI1O1q29iX3APY1WBJHchFQRkGTI1EmOdrF8mI25fAGyaERxiImAcHaueFJ1BASA1Y3M3HaynoTIKD1u0IHEGJx11pTuOqUIJFSEgpHWRGxEQIKt1ZJuRESE3ZUc5LH13nRqTpxRkpQqVJaSeIHyjo3uAGayeqmSerRkenKyHH3ALo2DlD080o0uCX1L5E09kpTp3nSEnraWjLmM4pRueX0kDFaMLHJb4ZTb1rJj0rUSjp1tmGmEEA1AvDHEHIIR3qIcmrxI0Zac1Z3RjLyy1pyR0GxZ0AUMAASA2ozS5ZxqnIRf2I0ADpSWKX3c1JJ5EMKblDzSuraESrJWjISWQG1LmDGWaXl8iM29hH0gZqIqBMItmYmqvE0Svq0V5A2kvBHA2p0EdqypmEvgFEKAAJxSGLmRkIJf4ZHqRJyumq1ZiEab1JTyZZJLmFHk4ZaucFvg2EFgUZUSgIKAjBQWTY3N4JGO2LGSmLyEzMGqnnTf3HSEnZyqWZyOzAQWDIPguImAIHHWSBGL3Ex9DrwWHX09DZQM2Y0WbX3IhGQyCGT9EXmN3AxSHHaEWMwL1MzplZUb2M1t0JSubFKbmD2IvoKuyMT1hBIElrx42qH9FEyAiBKEJIGuwpSMCLwOypwW0oKSkMUqTq24kGwSFFIOIoRAiFHSYqHyuASIAJxMdIwE0ZmyMDJyWoFf1AwSBraL4EUp9CFpcXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))