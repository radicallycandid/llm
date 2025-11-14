# Beabá da OpenAI API

Este projeto demonstra como usar a API da OpenAI através de três exemplos práticos, do básico ao criativo. Todos os scripts usam os modelos mais recentes da série GPT-5 (lançada em agosto de 2025), incluindo o GPT-5.1 (lançado em novembro de 2025).

## 📋 Pré-requisitos

- Python 3.9 ou superior
- Chave de API da OpenAI ([obtenha aqui](https://platform.openai.com/api-keys))
- Biblioteca `openai` versão 1.54.0 ou superior

## 🚀 Instalação

### 1. Clone ou baixe este repositório

```bash
git clone https://github.com/radicallycandid/llm.git
cd llm
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave de API

Crie um arquivo `.env` na raiz do projeto (use `.env.example` como template):

```bash
cp .env.example .env
```

Edite `.env` e adicione sua chave:

```
OPENAI_API_KEY=sua_chave_aqui
```

**Importante:** Nunca faça commit do arquivo `.env` com sua chave real!

## 📚 Scripts Disponíveis

### 1. `national_capitals.py` - Consulta de Capitais

Demonstra uso básico da API para perguntas factuais.

**Modelo:** `gpt-5-nano` (mais rápido e econômico para tarefas simples)

**Execução:**
```bash
python national_capitals.py
```

**Exemplo:**
```
Country: Brazil
Capital: Brasília
```

---

### 2. `text_summary.py` - Resumo de Textos

Demonstra como resumir arquivos de texto longos em um único parágrafo.

**Modelo:** `gpt-4.1-mini` (bom equilíbrio entre custo e capacidade)

**Execução:**
```bash
python text_summary.py
```

**Exemplo:**
```
File path: great_work.txt
⏳ Summarizing...

📝 Summary:
[Resumo gerado aqui]
```

**Arquivos de teste inclusos:**
- `great_work.txt` - Ensaio de Paul Graham sobre "How to Do Great Work"
- `managers_schedule_makers_schedule.txt` - Ensaio sobre calendários de gerentes vs. makers

---

### 3. `question_answering.py` - Respostas em Soneto

Demonstra uso criativo da API: respostas sempre em forma de soneto português, no estilo de Camões.

**Modelo:** `gpt-5.1` (melhor modelo para saída criativa/literária)

**Execução:**
```bash
python question_answering.py
```

**Exemplo:**
```
❓ Pergunta: O que é inteligência artificial?

✍️  Compondo soneto...

📜 Resposta:

[Soneto em português gerado aqui]
```

## 📊 Comparação de Modelos

| Modelo | Uso Recomendado | Script que Usa |
|--------|----------------|----------------|
| **gpt-5-nano** | Tarefas simples, factuais | `national_capitals.py` |
| **gpt-4.1-mini** | Resumos, classificação | `text_summary.py` |
| **gpt-5.1** | Raciocínio complexo, criatividade | `question_answering.py` |

## 🔗 Documentação Oficial

- **Visão Geral:** [OpenAI Platform Overview](https://platform.openai.com/docs/overview)
- **API Reference:** [Chat Completions](https://platform.openai.com/docs/api-reference/chat)
- **Guia de Chat:** [Chat Guide](https://platform.openai.com/docs/guides/chat-completions)
- **Modelos Disponíveis:** [Models Documentation](https://platform.openai.com/docs/models)
- **Melhores Práticas:** [Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)

## 🛡️ Segurança e Melhores Práticas

1. **Nunca exponha sua API key** - Use variáveis de ambiente
2. **Use `.gitignore`** - Já incluído para proteger `.env`
3. **Defina limites de uso** - Configure billing limits no dashboard da OpenAI
4. **Escolha o modelo certo** - Use modelos menores quando possível
5. **Ajuste `temperature`** - Use 0 para respostas determinísticas, 0.7-1.0 para criatividade
6. **Defina `max_tokens`** - Limite o tamanho das respostas

## 💡 Dicas

### Escolha do Modelo

- Para tarefas factuais simples: use `gpt-5-nano` (mais rápido)
- Para resumos e classificação: use `gpt-4.1-mini` (bom equilíbrio)
- Para raciocínio complexo e criatividade: use `gpt-5.1`
- Defina `max_tokens` apropriadamente para evitar respostas desnecessariamente longas

### Ajuste de `temperature`

```python
temperature=0      # Determinístico, ideal para fatos
temperature=0.3    # Pouca variação, bom para resumos
temperature=0.7    # Balanceado
temperature=1.0    # Muito criativo, variado
```

### Tratamento de Erros

Todos os scripts incluem tratamento robusto de erros:
- Erros de API (rate limits, autenticação)
- Erros de arquivo (não encontrado, encoding)
- Interrupções do usuário (Ctrl+C)

## 🐛 Solução de Problemas

**Erro: "No API key provided"**
- Certifique-se de que criou o arquivo `.env` com sua chave

**Erro: "Rate limit exceeded"**
- Você excedeu o limite de requisições. Aguarde ou aumente seu plano

**Erro: "Invalid model"**
- Verifique se está usando um nome de modelo válido
- Consulte: https://platform.openai.com/docs/models

## 📄 Estrutura do Projeto

```
llm/
├── README.md                              # Este arquivo
├── requirements.txt                       # Dependências Python
├── .gitignore                            # Arquivos ignorados pelo Git
├── .env.example                          # Template para configuração
├── national_capitals.py                  # Script 1: Capitais
├── text_summary.py                       # Script 2: Resumos
├── question_answering.py                 # Script 3: Sonetos
├── great_work.txt                        # Arquivo de teste
└── managers_schedule_makers_schedule.txt # Arquivo de teste
```

## 📝 Licença

Este projeto é de código aberto para fins educacionais.

## 👤 Autor

**radicallycandid**
- GitHub: [@radicallycandid](https://github.com/radicallycandid)

## 🙏 Créditos

- Arquivos de teste: ensaios de [Paul Graham](http://paulgraham.com)
- API: [OpenAI Platform](https://platform.openai.com)

---

**Última atualização:** Novembro 2025
**Modelos usados:** gpt-5-nano, gpt-4.1-mini, gpt-5.1
