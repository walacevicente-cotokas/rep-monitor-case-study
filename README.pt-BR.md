# REP-Monitor — Estudo de caso de monitoramento corporativo

**[English](README.md) | [Arquitetura](docs/architecture.md) | [Decisões técnicas](docs/engineering-decisions.md) | [Exemplos sanitizados](examples/)**

> Portfólio técnico com documentação de um sistema empresarial real. Este repositório **não** disponibiliza os fontes de produção nem acesso ao ambiente corporativo.

## O desafio
Técnicos e supervisores precisavam consultar equipamentos de impressão, reconhecer falhas de coleta, cruzar registros do ERP com monitoramento e realizar diagnóstico sem depender de múltiplas ferramentas.

## A solução
A plataforma reúne **aplicativo Flutter para Android, portal Next.js, API FastAPI, banco PostgreSQL 15, integrações SOAP/REST e implantação em Google Cloud Run**. Entre as funcionalidades documentadas estão busca por REP/serial, status de coleta, históricos, indicadores, mapas com clusters, revalidação, relatórios e administração de acessos.

## O que este case demonstra
- **Desenvolvimento mobile e web:** interfaces usadas em fluxos operacionais reais.
- **Backend e integrações:** API, autenticação, sincronização de dados, validação e tratamento de erros.
- **Banco de dados:** consultas SQL, conciliação ERP × coleta e histórico de transições.
- **Infraestrutura e operações:** Cloud Run, conectividade, processos agendados e diagnóstico em Windows Server.
- **Tomada de decisão:** seleção de locais problemáticos no mapa, revisão de importações e segurança de acesso.

O [README em inglês](README.md) reúne os links técnicos e o diagrama completo.

## Segurança e transparência
Repositórios da empresa continuam privados. Os exemplos deste portfólio são **ilustrativos e escritos com dados fictícios**, sem copiar trechos proprietários. Números operacionais e telas reais só serão publicados mediante revisão e autorização. Este material não afirma autoria individual exclusiva de todo o produto.

**Autor do case:** [Walace Silva Vicente](https://github.com/walacevicente-cotokas) · [LinkedIn](https://www.linkedin.com/in/walace-silva-8a14b1a0/)
