import openai

openai.api_key = "SUA_CHAVE_AZURE_OPENAI"

# Mercado de Seguros
response = openai.Completion.create(
    engine="gpt-4",
    prompt="Gere uma apólice de seguro de carro para um cliente com cobertura total.",
    temperature=0.5,
    max_tokens=500
)

print(response.choices[0].text.strip())

#Jurídico
response = openai.Completion.create(
    engine="gpt-4",
    prompt="Resuma os principais pontos da Lei Geral de Proteção de Dados (LGPD) para um advogado.",
    temperature=0.3,
    max_tokens=300
)

print(response.choices[0].text.strip())

# Cripto
response = openai.Completion.create(
    engine="gpt-4",
    prompt="Explique o conceito de proof-of-stake (PoS) e sua importância no Ethereum 2.0.",
    temperature=0.7,
    max_tokens=400
)

print(response.choices[0].text.strip())
