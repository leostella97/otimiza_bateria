# Otimiza carregamento da bateria

Este código em Python utiliza a biblioteca Tkinter para criar uma interface gráfica simples que permite otimizar o carregamento da bateria do notebook. Abaixo está uma explicação detalhada do código:

## Funções:

### `carregar_bateria()`:
- Obtém o status atual da bateria usando a biblioteca `psutil`.
- Se a porcentagem da bateria estiver abaixo de 85%, chama o método `charge()` para carregar a bateria.

### `descarregar_bateria()`:
- Obtém o status atual da bateria usando a biblioteca `psutil`.
- Se a porcentagem da bateria estiver acima de 80%, chama o método `discharge()` para descarregar a bateria.

### `iniciar_script()`:
- Inicia o script de otimização da bateria.
- Carrega a bateria até 85%.
- Enquanto a bateria estiver acima de 80%, descarrega até 80% e repete o processo.
- Volta a carregar a bateria até 85%.

### `sair()`:
- Encerra o programa ao destruir a janela principal.

## Interface Gráfica:

- Cria uma janela principal (`janela`) usando Tkinter com o título "Otimização de carregamento".
- Define uma fonte bold de tamanho 16 para uso posterior na interface gráfica.
- Cria um rótulo no topo da janela com o texto "Otimização de carregamento" usando a fonte definida.
- Cria um segundo rótulo no centro da janela com instruções sobre o processo de otimização da bateria.
- Cria um botão "INICIAR" que, quando clicado, executa a função `iniciar_script`.
- Cria um botão "SAIR" que, quando clicado, executa a função `sair`.
- Cria um rótulo no rodapé da janela com o texto "Desenvolvido por Leonardo Stella" usando uma fonte itálica de tamanho 16.
- Define o comportamento da janela quando minimizada para não fechar o programa.
- Inicialmente, minimiza a janela e a retira da área de trabalho.
- Mostra a janela principal.

Este código cria uma aplicação simples que oferece uma maneira automatizada de carregar e descarregar a bateria do notebook, seguindo critérios específicos, visando otimizar a vida útil da bateria.
