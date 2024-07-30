# Implementação do Algoritmo de Bresenham e plotagem

## Pré-requisitos
- Linux
- Git
- Python 3 (Versão utilizada: 3.12.4)

## Em caso de possível erro
Um erro que obtive foi OpenGL.error.NullFunctionError: Attempt to call an undefined function glutInit, check for bool(glutInit) before calling

Para resolver no linux é só executar o seguinte comando:

```sudo apt-get install freeglut3-dev```


## Observação
O cálculo dos pontos da plotagem e exibição para prova do algoritmo estão para os pontos (1, 1) e (8, 5), pois foram os pedidos na atividade, mas para plotagem do gráfico estou multiplicando o (8, 5) por um escalar para ter uma visualização melhor da reta. Caso não desejar a multiplicação pelo escalar é só modificar no código.

## Instalação
- No seu terminal clone o repositório: ```git clone https://github.com/fernandogfleite/CG.git```

- Entre na pasta do repositório: ```cd CG```

- Crie uma virtualenv: ```python -m venv venv```

- Ative a virtualenv: ```source venv/bin/activate```

- Instale as dependências: ```pip install -r requirements.txt```

## Executar
- Para executar a plotagem: ```python main.py```
- Para executar o algoritmo de forma independente e obter os pontos para plotagem: ```python algorithms/bresenham_algorithm.py```


