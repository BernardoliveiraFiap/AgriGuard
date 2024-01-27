def InformarTratamento():
      
      spodovir = ('\n---Tratamento para a sua plantação: Spodovir---'
                  '\n1. É um biodefensivo e inseticida microbiológico'
                  '\n2. Deve ser utilizado assim que a praga for identificada ou de 10 a 22 dias após a germinação das plantações'
                  '\n3. É recomendado pulverizar o produto sobre a cultura com a utilização do volume da calda de 150 litros do produto por hectare se for por via terrestre ou 50 litros do produto por hectare se for por via aérea'
                  '\n4. Uma dose pode ser diluída em 1 litro de água'
                  '\n5. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      engeoPlenoS = ('\n---Tratamento para a sua platação: Engeo Pleno S---'
                     '\n1. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.') 
      
      bacillus = ('\n---Tratamento para a sua plantação: Bacillus Thuringienses---'
                  '\n1. É um inseticida biológico'
                  '\n2. Recomendação de pulverização sobre a cultura com a utilização de 500 a 750 gramas por hectare, sendo a utilização do volume da calda de 200 litros por hectare'
                  '\n3. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      aug = ('\n---Tratamento para a sua plantação: AUG 106---'
             '\n1. É um inseticida de suspensão concentrada'
             '\n2. Para informações de como fazer, precauções e mais, leia a bula que vem junto ao produto no momento da compra.')
      
      nomePlanta = input('\nQual o nome da plantação atacada? ')
      nomePraga = input('Qual o nome da praga? ')

      
      nomePraga = nomePraga.upper()

      #Algodão
      if nomePlanta == 'ALGODÃO' or nomePlanta == 'ALGODAO':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
      
            elif nomePraga == 'PERCEVEJO-MARROM' or nomePraga == 'PERCEVEJO MARROM':
                  return f'{engeoPlenoS}\nObservação: de 200 a 250 mL por hectare com no máximo 3 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare'
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  return bacillus
            
            elif nomePraga == 'PULGÃO DO ALGODOEIRO' or nomePraga == 'PULGAO DO ALGODOEIRO':
                  return f'{aug}\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.'
            
            elif nomePraga == 'TRIPES':
                  return f'{aug}\nObservação: de 540 a 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.'
            
            elif nomePraga == 'CUPIM DE MONTÍCULO' or nomePraga == 'CUPIM DE MONTICULO':       
                  return f'{aug}\nObservação: 720 mL a cada 100kg com no máximo 1 aplicação; o volume da calda deve ser de 500mL a cada 100kg.'
            else:
                  return '\nEssa praga não está em nosso sistema'
      

      #Arroz
      elif nomePlanta == 'ARROZ':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-DO-ARROZ' or nomePraga == 'PERCEVEJO DO ARROZ':
                  return f'{engeoPlenoS}\nObservação: de 150 a 200 mL por hectare com no máximo 1 aplicação; o volume da calda deve ser de 200 litros por hectare'
            else:
                  return '\nEssa praga não está em nosso sistema'
      

      
      elif nomePlanta == 'AVEIA':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
            else:
                  return '\nEssa praga não está em nosso sistema'
      

      
      elif nomePlanta == 'CAFÉ' or nomePlanta == 'CAFE':
            if nomePraga == 'LAGARTA HELICOVERPA':
                  return bacillus
            else:
                  return '\nEssa praga não está em nosso sistema'


      
      elif nomePlanta == 'CANA-DE-AÇÚCAR' or nomePlanta == 'CANA-DE-AÇUCAR' or nomePlanta == 'CANA-DE-ACUCAR' or nomePlanta == 'CANA DE AÇÚCAR' or nomePlanta == 'CANA DE AÇUCAR' or nomePlanta == 'CANA DE AÇUCAR' or nomePlanta == 'CANA DE ACUCAR':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
            else:
                  return '\nEssa praga não está em nosso sistema'
      

      
      elif nomePlanta == 'FEIJAO' or nomePlanta == 'FEIJÃO':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  return bacillus
            else:
                  return '\nEssa praga não está em nosso sistema'
      

      
      elif nomePlanta == 'GIRASSOL':
            if nomePraga == 'PERCEVEJO-VERDE-PEQUENO' or nomePraga == 'PERCEVEJO VERDE PEQUENO':
                  return f'{engeoPlenoS}\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare'
            
            elif nomePraga == 'PERCEVEJO-DA-SOJA' or nomePraga == 'PERCEVEJO DA SOJA':
                  return f'{engeoPlenoS}\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare'
            
            elif nomePraga == 'PERCEVEJO-MARROM' or nomePraga == 'PERCEVEJO MARROM':
                  return f'{engeoPlenoS}\nObservação: de 300 a 400 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 150 litros por hectare'
            else:
                  return '\nEssa praga não está em nosso sistema'
      
      
      #Milho
      elif nomePlanta == 'MILHO':
            if nomePraga == 'PERCEVEJO-BARRIGA-VERDE' or nomePraga == 'PERCEVEJO BARRIGA VERDE':
                  return f'{engeoPlenoS}\nObservação: de 150 a 250 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare'
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  return bacillus
            
            elif nomePraga == 'CIGARRINHA DO MILHO':
                  return f'{aug}\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg'
            
            elif nomePraga == 'VAQUINHA VERDE AMARELA':
                  return f'{aug}\nObservação: 960 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg'
            
            elif nomePraga == 'CUPIM':
                  return f'{aug}\nObservação: 300 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg'
            
            elif nomePraga == 'PULGÃO' or nomePraga == 'PULGAO':
                  return f'{aug}\nObservação: 480 mL para cada 100kg com apenas uma aplicação; o volume da calda deve ser 500 mL para cada 100kg'
            else:
                  return '\nEssa praga não está em nosso sistema'
      

      #Soja
      elif nomePlanta == 'SOJA':
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-MARROM' or nomePraga == 'PERCEVEJO MARROM':
                  return f'{aug}\nObservação: 200 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare.'
            
            elif nomePraga == 'PERCEVEJO-VERDE-PEQUENO' or nomePraga == 'PERCEVEJO VERDE PEQUENO':
                  return f'{aug}\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare'
            
            elif nomePraga == 'PERCEVEJO-DA-SOJA' or nomePraga == 'PERCEVEJO DA SOJA':
                  return f'{aug}\nObservação: de 150 a 180 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare'
            
            elif nomePraga == 'LAGARTA HELICOVERPA':
                  return bacillus
            else:
                  return '\nEssa praga não está em nosso sistema'


      #Trigo
      elif nomePlanta == 'TRIGO':
            nomePraga = nomePraga.upper()
            if nomePraga == 'LAGARTA-DO-CARTUCHO' or nomePraga == 'LAGARTA DO CARTUCHO':
                  return spodovir
            
            elif nomePraga == 'PERCEVEJO-BARRIGA-VERDE' or nomePraga == 'PERCEVEJO BARRIGA VERDE':
                  return f'{engeoPlenoS}\nObservação: 150 mL por hectare com no máximo 2 aplicações, uma a cada 7 dias; o volume da calda deve ser de 200 litros por hectare'
            else:
                  return '\nEssa praga não está em nosso sistema'
      else:
            return '\nEssa planta não está em nosso sistema'



def Cadastro():
      confirmCadastroup = ''
      print('\nPor favor realize o cadastro: ')
      while confirmCadastroup != "1" and confirmCadastroup != "SIM":
            opcIdentup = ''
            opcIdent2up = ''
            opcComplementoup = ''
            confirmCadastroup = ''
            rg = ''
            telefone = ''
            cep = ''
            cnh = ''
            NomeCompleto = ''
            email = ''
            rua = ''
            nmrResidencia = ''
            pais = ''
            estado = ''
            cidade = ''
            bairro = ''

            #Para o usuário informar suas informações ao sistema
            while NomeCompleto == '':
                  NomeCompleto = input("\nDigite seu nome: ")
            while opcIdentup != "1" and opcIdentup != "RG" and opcIdentup != "2" and opcIdentup != "CNH":
                  opcIdent = input("\n(1) - RG \n(2) - CNH \nEscolha qual você deseja informar: ")
                  opcIdentup = opcIdent.upper()
                  if opcIdentup == "1" or opcIdentup == "RG":
                        while len(rg) != 9:      
                              rg = input("\nRG: ")
                              if  len(rg) != 9:
                                    print("Digite um RG válido com 9 números e sem indicadores.")
                  elif opcIdentup == "2" or opcIdentup == "CNH":
                        while len(cnh) != 10:
                              cnh = input("\nCNH: ")
                              if len(cnh) != 10:
                                    print("Digite uma CNH válida com 10 números e sem indicadores.")

            while opcIdent2up != "1" and opcIdent2up != "CPF" and opcIdent2up and "2" and opcIdent2up != "CNPJ":
                  opcIdent2 = input("\n(1) - CPF \n(2) - CNPJ \nEscolha qual você deseja informar: ")
                  opcIdent2up = opcIdent2.upper()
                  if opcIdent2up == "1" or opcIdent2up == "CPF":
                        while len(cpf) != 11:
                              cpf = input("\nCPF: ")
                              if len(cpf) != 11:
                                    print("Digite um CPF válido com 11 números e sem indicadores.")
                  elif opcIdent2up == "2" or opcIdent2up == "CNPJ":
                        while len(cnpj) != 14:
                              cnpj = input("\nCNPJ: ")
                              if len(cnpj) != 14:
                                    print("Digite um CNPJ válido com 14 números e sem indicadores.")

            while email == "": 
                  email = input("\nE-mail: ")
            while len(telefone) != 14:
                  telefone = input("\nTelefone: ")
                  if len(telefone) != 14:
                        print("Digite um telefone válido. Ex(+5511999999999).")
            while rua == "":
                  rua = input("\nRua: ")
            while nmrResidencia == "":
                  nmrResidencia = input("\nNúmero de Residência: ")
            while opcComplementoup != "1" and opcComplementoup != "SIM" and opcComplementoup != "2" and opcComplementoup != "NAO" and opcComplementoup != "NÃO":
                  opcComplemento = input("\n(1) - Sim \n(2) - Não \nDeseja informar um complemento?: ")
                  opcComplementoup = opcComplemento.upper()
                  if opcComplementoup == "1" or opcComplementoup == "SIM":
                        complemento = input("\nComplemento: ")
                  elif opcComplementoup == "2" or opcComplementoup == "NAO" or opcComplementoup == "NÃO":
                        print("")
            while pais == "":
                  pais = input("\nPaís: ")
            while estado == "":
                  estado = input("\nEstado: ")
            while cidade == "":
                  cidade = input("\nCidade: ")
            while bairro == "":
                  bairro = input("\nBairro: ")
            while len(cep) !=8:
                  cep = input("\nCEP: ")
                  if len(cep) != 8:
                        print("Digite um CEP válido com 8 números e sem indicadores.")
            print("\nConfirme as informações: ")

            
            while confirmCadastroup != "1" and confirmCadastroup != "SIM" and confirmCadastroup != "2" and confirmCadastroup != "NAO" and confirmCadastroup != "NÃO" :
            
                  print("\n--- Dados Pessoais ---")
                  print(f"Nome:  {NomeCompleto}")
                  if opcIdentup == "1" or opcIdentup == "RG":
                        print(f"RG: {rg}")
                  if opcIdentup == "2" or opcIdentup == "CNH":
                        print(f"CNH: {cnh}")
                  if opcIdent2up == "1" or opcIdent2up == "CPF":
                        print(f"CPF: {cpf}")
                  if opcIdent2up == "2" or opcIdent2up == "CNPJ":
                        print(f"CNPJ: {cnpj}")
                  print(f"E-mail: {email}")
                  print(f"Telefone: {telefone}")

                  print("\n--- Endereço ---")
                  print(f"Rua: {rua}")
                  print(f"Número de Residência: {nmrResidencia}")
                  if opcComplementoup == "1" or opcComplementoup == "SIM":
                        print(f"Complemento: {complemento}")
                  print(f"País: {pais}")
                  print(f"Estado: {estado}")
                  print(f"Cidade: {cidade}")
                  print(f"Bairro: {bairro}")
                  print(f"CEP: {cep}")

                  #Para confirmar o cadastro
                  confirmCadastro = input("\n(1) - Sim \n(2) - Não \nOs dados estão corretos? \nEscolha uma opção: ")
                  confirmCadastroup = confirmCadastro.upper()
                  if confirmCadastroup == "1" or confirmCadastroup == "SIM": 
                        print("Concluímos seu cadastro!")
                  elif confirmCadastroup == "2" or confirmCadastroup == "NAO" or confirmCadastroup == "NÃO":
                        print("Faça novamente o cadastro!")

      
      qntdDrone = int(input("\nQuantos drones você deseja comprar? \nDrones: "))

      if qntdDrone > 0 and qntdDrone < 999:
            print(f"Obrigado pela compra! Seus {qntdDrone} drones chegarão em até 15 dias úteis.")
            print("Lembrando que foi apenas uma simulação, a PlanTech está em desenvolvimento portanto os drones não serão enviados.")
      else:
            print("O limite de drones é de 1 a 999.")


def IndicarTratamento():
      print('\n--Preencha as informações: ---')

      nomePraga = input('Nome da praga: ')
      tipoPlantacao = input('Nome da plantação que ela ataca: ')
      tratamento = input('Tipo de tratamento que a praga e a plantação devem receber: ')
      return "\nObrigado pelas informações. Elas serão analisadas e, se estiverem corretas, serão incluídas no sistema PlanTech."



opcaoMenu = 0
while opcaoMenu != 9:
      print('\nSeja bem vindo à PlanTech! No que podemos te ajudar?'
            '\n'
            '\n1. Desejo saber mais sobre a missão da PlanTech'
            '\n2. Desejo saber sobre o funcionamento do drone'
            '\n3. Quero comprar um drone para detectar pragas'
            '\n4. Identifiquei uma praga na plantação. O que faço agora?'
            '\n5. Quem faz parte do projeto PlanTech?'
            '\n6. Quero indicar um tratamento para uma praga'
            '\n7. Feedback'
            '\n8. Outro'
            '\n9. Encerrar')
      opcaoMenu = int(input('Selecione uma das opções acima: '))


      if opcaoMenu == 1:
            print('\n---- PlanTech ----'
                        + '\n A fome e a insegurança alimentar são problemas mundiais que afetam milhões de pessoas.'
                        + '\n Isto acarreta em outros problemas, como o nanismo e a caquexia.'
                        + '\n São muitos os fatores que podem levar à fome, tais como a falta de agricultura sustentável, falta de acesso à alimentos, desigualdades, desemprego, alimentos não-nutritivos, entre outros fatores.'
                        + '\n Pensando nisso, a PlanTech desenvolveu um projeto que visa a diminuição do desperdício de alimentos e o cultivo de alimentos mais saudáveis com o combate de pragas ainda em sua fase inicial de ataque nas plantações.'
                        + '\n\n Os benefícios dessa tecnologia é a detecção da praga em fase inicial, o que reduz:'
                        + '\n 1. O nível de perda de alimentos' 
                        + '\n 2. O valor do produto final'
                        + '\n 3. A preservação do solo e das plantações'
                        + '\n 4. A garantia de uma alimentação saudável e nutritiva'
                        + '\n\n Essa tecnologia pode ser levada para agricultores familiares e regiões mais afastadas que muito sofrem com esse problema'
                        + '\n Dessa forma, contribuirá com o acesso à uma tecnologia capaz de diminuir suas perdas de alimentos por pragas.'
                        + '\n Além disso, estes pequenos agricultores se sentirão mais confiantes e seguros em expandir sua área de plantio.')



      if opcaoMenu == 2:
            print("\n----PlanTech ----"
                        + '\n Será desenvolvido um drone robô que detecta pragas nas plantações e informa suas localidades para o combate.'
                        + '\n Essa detecção é por meio de uma IA generativa que identifica as pragas com infravermelho ainda na fase inicial.'
                        + '\n Depois de detectar, ela informa o nome da praga e o seu local no visor do drone.'
                        + '\n Com essa informação, basta entrar no sistema da PlanTech e informar o nome da praga e qual plantação ela está atacando.'
                        + '\n Assim será indicado um tratamento saudável e sustentável para que a plantação não seja perdida, danificada e nem tenha alastramento das pragas.'
                        + '\n Este drone funciona sozinho e é recarregável, sendo necessário somente ligá-lo para que sobrevoe a plantação em busca de possíveis pragas.'
                        + '\n O usuário pode também entrar em contato com o nosso ChatBot para solucionar possíveis dúvidas, dar seu feedback e ir no site da PlanTech para mais informações sobre agricultura ou semelhantes. '
                        + '\n Além disso, o agricultor pode contribuir com informações de pragas e tratamentos que não tenham no site.')



      if opcaoMenu == 3:
            print("\nA PlanTech ainda é um projeto em desenvolvimento e, por isso, não é possível realizar a compra dos drones.")
            opcSimulacao = input("\nDeseja realizar uma simulação da compra dos drone que serão disponibilizados pela PlanTech? \n(1) - Sim \n(2) - Não \nEscolha uma opção: ")
            opcSimulacaoup = opcSimulacao.upper()
            if opcSimulacaoup == "1" or  opcSimulacaoup == "SIM":
                 Cadastro()



      if opcaoMenu == 4:
            print(InformarTratamento())



      if opcaoMenu == 5:
            print('\n---Responsáveis pelo projeto PlanTech---'
                  +' \n Douglas Magalhães de Araujo - rm552008'
                  +' \n Gustavo Arguello Bertacci - rm551304' 
                  +' \n Igor Ribeiro Anccilotto - rm550415'
                  +' \n Luiz Fillipe Farias - rm99519' 
                  +' \n Rafaella Monique do Carmo Bastos - rm552425')



      if opcaoMenu == 6:
            print(IndicarTratamento())
            


      if opcaoMenu == 7:
           
            feedback = int(input('\nPrimeiro, informe o tipo do feedback: '
                              +'\n (1) - Resolução de suas dúvidas'
                              +'\n (2) - Performace do sistema' 
                              +'\n (3) - Indicação dos tratamentos para as plantações' 
                              +'\n (4) - Usabilidade do projeto' 
                              +'\n (5) - Experiência com o site'
                              +'\n -Opção: '))
            
            
            if feedback < 1 or feedback > 5:
                  print('Escolha incorreta! Escolha um número de 1 a 5.')

            #O usuário digita a nota do feedback de 0 até 10, e depois escreve uma observação.
            elif feedback == 1:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  
                  #Se o usuário digitar um número maior que 10 ou menor que 0, aparece uma mensagem de erro.
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')

            elif feedback == 2:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')

            elif feedback == 3:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')

            elif feedback == 4:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')

            elif feedback == 5:
                  notaFeedback = int(input('Digite a nota que desejar (0-10): '))
                  if notaFeedback < 0 or notaFeedback > 10:
                        print('Os números permitidos são apenas de 0 a 10!')
                  else:
                        reclamacao = input('Escreva sua reclamação ou aperte ENTER para enviar: ')
                        print(f'\nA PlanTech agradece pelo seu feedback!')



      if opcaoMenu == 8:
            print('\nVeja só:')
            print('1. Se quiser retirar suas dúvidas mais específicas, entre no nosso ChatBot que ele te auxiliará')
            print('2. Se quer textos mais explicativos como agricultura, IAs generativas ou outros textos, entre no site da PlanTech')



      if opcaoMenu == 9:
            print('\nMuito obrigado, até a próxima!')