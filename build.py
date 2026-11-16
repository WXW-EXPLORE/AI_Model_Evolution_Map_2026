import json,csv,datetime,html,pathlib
ROOT=pathlib.Path('/mnt/data/AI_Model_Evolution_Map_2026')
M=[]
def add(f,n,d,tags,access='API',arch='未公开',desc='',src='',parent=None,scale='',evidence='官方资料',region=None):
    M.append(dict(id=f'{f}-{len(M)+1}',family=f,name=n,date=d,skills=tags.split('/'),access=access,architecture=arch,summary=desc,source=src or FAMILY_SRC.get(f,''),parent=parent,scale=scale,evidence=evidence,region=region))
FAMILY_SRC={
'OpenAI':'https://openai.com/research/index/release/','Anthropic':'https://www.anthropic.com/news/models',
'Google Gemini':'https://ai.google.dev/gemini-api/docs/models','Meta Llama':'https://ai.meta.com/blog/llama-4-multimodal-intelligence/',
'Alibaba Qwen':'https://github.com/QwenLM/Qwen3.8','DeepSeek':'https://api-docs.deepseek.com/updates/',
'Mistral':'https://mistral.ai/news/','Google Gemma':'https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/',
'Moonshot Kimi':'https://github.com/MoonshotAI/Kimi-K2.5','Z.ai GLM':'https://github.com/zai-org/GLM-5',
'Microsoft Phi':'https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/',
'Ai2 OLMo':'https://allenai.org/blog/olmo3','NVIDIA Nemotron':'https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/',
'Meta Muse':'https://ai.meta.com/research','技术源流':'https://arxiv.org/abs/1706.03762'}
# tags: R 推理, C 编码, V 多模态, L 长上下文, E 效率/端侧, A Agent, Z 中文/多语, O 开放/可研究, S 科学
# dates official launch month, selected month-level verified or marked display inferred only for certain releases
add('技术源流','Transformer','2017-06','O/L','论文','Transformer','Attention Is All You Need；现代 Transformer 模型架构起点。','https://arxiv.org/abs/1706.03762')
add('技术源流','BERT','2018-10','O/Z','论文/开源','Encoder','双向预训练 / 编码器方向，非今天生成式 LLM 的直接父模型。','https://arxiv.org/abs/1810.04805')
add('技术源流','GPT-1','2018-06','O','论文','Decoder-only','生成式预训练 Transformer 代表性早期工作。','https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf')
add('技术源流','T5','2019-10','O/Z','论文/开源','Encoder–decoder','Text-to-Text 统一任务范式。','https://arxiv.org/abs/1910.10683')
add('技术源流','Mamba','2023-12','E/L/O','论文/开源','SSM','选择性状态空间模型；代表注意力之外的序列建模路线。','https://arxiv.org/abs/2312.00752')
add('技术源流','RWKV','2023-05','E/L/O','开放权重','RNN-like','线性复杂度的递归与 Transformer 融合设计；作为替代架构类别。','https://github.com/BlinkDL/RWKV-LM')
add('OpenAI','GPT-2','2019-02','O/C','历史开放权重','Dense decoder','生成式预训练里程碑。','https://openai.com/index/better-language-models/')
add('OpenAI','GPT-3','2020-05','Z/C','API','Dense decoder','规模化 few-shot learning 的标志性工作。','https://arxiv.org/abs/2005.14165')
add('OpenAI','InstructGPT','2022-01','Z','论文/API','RLHF','指令对齐路线的重要里程碑。','https://openai.com/index/instruction-following/')
add('OpenAI','GPT-3.5 / ChatGPT','2022-11','Z/A','API','未公开','对话助手大规模应用拐点；ChatGPT 是产品，不等于一个固定 checkpoint。','https://openai.com/index/chatgpt/')
add('OpenAI','GPT-4','2023-03','R/C','API','未公开','强通用推理与代码能力。','https://openai.com/index/gpt-4-research/')
add('OpenAI','GPT-4o','2024-05','V/Z','API','未公开','原生音频交互与多模态响应方向。','https://openai.com/index/hello-gpt-4o/')
add('OpenAI','o1','2024-09','R/S','API','未公开','强化推理时计算路径，2024-09 首发 preview。','https://openai.com/index/introducing-openai-o1/')
add('OpenAI','o3 / o4-mini','2025-04','R/C/A','API','未公开','工具使用与推理增强的一组模型。','https://openai.com/index/introducing-o3-and-o4-mini/')
add('OpenAI','GPT-5','2025-08','R/C/A','API','系统：快速+深思考+路由','按任务智能路由，是系统形态，不宜误认单一 checkpoint。','https://openai.com/index/introducing-gpt-5/')
add('OpenAI','GPT-5.6 Sol','2026-07','R/C/S/A','API','未公开','复杂科学、代码与工程推理取向。','https://help.openai.com/en/articles/9624314-model-release-notes')
add('OpenAI','GPT-6 Astra','2026-09','R/C/A/S/V','API','未公开','专业工作、工程任务、计算机使用的旗舰分支。','https://openai.com/index/gpt-6-astra/')
add('OpenAI','GPT-6 Sol / Luna','2026-09','R/C/E','API','未公开','同代高能力与更经济的产品层次。','https://openai.com/index/introducing-gpt-6-sol-and-luna/')
add('OpenAI','GPT-6.1 Sol','2026-09','R/C/A/E','API','未公开','能力/成本折中、面向工程与任务执行。','https://openai.com/research/index/release/')
add('OpenAI','GPT-6.1 Terra','2026-10','V/A/E','API','未公开','计算机使用、视觉交互效率方向。','https://openai.com/research/index/release/')
add('Anthropic','Claude 1','2023-03','Z','API','未公开','Claude 系列商业发布。','https://www.anthropic.com/news/introducing-claude')
add('Anthropic','Claude 2','2023-07','Z/L','API','未公开','长文本处理与助手能力演进。','https://www.anthropic.com/news/claude-2')
add('Anthropic','Claude 3 (Opus/Sonnet/Haiku)','2024-03','V/R/E','API','未公开','能力/成本/速度三级模型家族。','https://www.anthropic.com/news/claude-3-family')
add('Anthropic','Claude 3.5 Sonnet','2024-06','C/V','API','未公开','代码与视觉能力提升，开启 Sonnet 工程路线。','https://www.anthropic.com/news/claude-3-5-sonnet')
add('Anthropic','Claude 3.7 Sonnet','2025-02','R/C/A','API','混合推理','较早的混合推理服务；同日 Claude Code 首次发布。','https://www.anthropic.com/news/claude-3-7-sonnet')
add('Anthropic','Claude 4 (Opus/Sonnet)','2025-05','C/R/A','API','未公开','长程编码、Agent 工作流取向。','https://www.anthropic.com/news/claude-4')
add('Anthropic','Claude Opus 4.5','2025-11','C/R/A','API','未公开','面向复杂编码与长程任务的 Opus 演进。','https://www.anthropic.com/system-cards')
add('Anthropic','Claude Opus 5.5','2026-09','C/R/A','API','未公开','Agentic Coding 与专业工作旗舰。','https://www.anthropic.com/news/models')
add('Anthropic','Claude Sonnet / Haiku 5.5','2026-10','C/A/E','API','未公开','分别面向工程均衡与高吞吐小模型（分别发布于 9 月、10 月）。','https://www.anthropic.com/news/models')
add('Anthropic','Claude Fable 5.2','2026-11','R/C/S','API','未公开','极难技术工作、科学/金融/编程；Mythos 同期受限访问。','https://www.anthropic.com/news/models')
add('Google Gemini','PaLM 2','2023-05','Z/R','API','未公开','Google PaLM 语言路线，Gemini 系列之前的重要一代。','https://blog.google/technology/ai/google-palm-2-ai-large-language-model/')
add('Google Gemini','Gemini 1.0','2023-12','V/R','API','未公开','原生多模态模型家族起点。','https://blog.google/technology/ai/google-gemini-ai/')
add('Google Gemini','Gemini 1.5 Pro','2024-02','L/V','API','未公开','长上下文处理成为核心竞争维度。','https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/')
add('Google Gemini','Gemini 2.0 Flash','2024-12','V/A/E','API','未公开','多模态和 agentic 时代的低延迟 Flash 系列。','https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/')
add('Google Gemini','Gemini 2.5 Pro','2025-03','R/V/L','API','未公开','思考能力与长上下文多模态演进。','https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/')
add('Google Gemini','Gemini 3 Pro','2025-11','R/V/A','API','未公开','多模态深推理/Agent 融合。','https://blog.google/products-and-platforms/products/gemini/gemini-3/')
add('Google Gemini','Gemini 3.1 Pro','2026-02','R/S/V','API','未公开','复杂科学和工程推理路线。','https://blog.google/innovation-and-ai/products/gemini-app/gemini-drop-february-2026/')
add('Google Gemini','Gemini 3.8 Flash','2026-09','A/C/V/E','API','未公开','长程软件工程与复杂自主 Agent 的 Flash 路线。','https://ai.google.dev/gemini-api/docs/changelog')
add('Meta Llama','LLaMA 1','2023-02','O/E','开放权重（受限）','Dense decoder','学术开放模型生态的重要开端。','https://arxiv.org/abs/2302.13971')
add('Meta Llama','Llama 2','2023-07','O/Z','开放权重（社区许可）','Dense decoder','研究与商业开放权重生态的标志性版本。','https://ai.meta.com/blog/llama-2/')
add('Meta Llama','Llama 3','2024-04','O/Z/C','开放权重（社区许可）','Dense decoder','开放权重通用模型大迭代。','https://ai.meta.com/blog/meta-llama-3')
add('Meta Llama','Llama 3.1 (405B)','2024-07','O/L/Z','开放权重（社区许可）','Dense decoder','405B 大模型与长上下文系列。','https://ai.meta.com/blog/meta-llama-3-1/')
add('Meta Llama','Llama 3.3','2024-12','O/E','开放权重（社区许可）','Dense decoder','70B 效率/质量权衡路线。','https://www.llama.com/')
add('Meta Llama','Llama 4 Scout/Maverick','2025-04','O/V/L/E','开放权重（社区许可）','MoE','原生图文多模态与 MoE；Scout 具超长上下文。','https://ai.meta.com/blog/llama-4-multimodal-intelligence/')
add('Meta Muse','Muse Spark 1.1','2026-07','C/A/V','API','未公开','Meta 新 Muse 系列 Agent/代码/多模态模型。','https://ai.meta.com/research')
add('Meta Muse','Muse Spark 1.3','2026-09','C/A','API','未公开','长程 coding 与个人 Agent 路线。','https://ai.meta.com/research')
add('Meta Muse','Muse Wonder','2026-10','R/C/A','API','未公开','高端专业任务与 Agentic coding。','https://ai.meta.com/research')
add('Alibaba Qwen','Qwen 1','2023-08','Z/O','开放权重','Dense decoder','中文/多语重要基础模型系列起点。','https://github.com/QwenLM/Qwen')
add('Alibaba Qwen','Qwen1.5','2024-02','Z/O/E','开放权重','Dense + MoE','多尺寸开放模型，以及量化支持。','https://qwenlm.github.io/blog/qwen1.5/')
add('Alibaba Qwen','Qwen2','2024-06','Z/O/C','开放权重','Dense + MoE','多语言与代码/数学扩展。','https://qwenlm.github.io/blog/qwen2/')
add('Alibaba Qwen','Qwen2.5 / Coder / Math','2024-09','Z/C/R/O','开放权重','Dense decoder','7B/14B/32B/72B 等与代码、数学专用分支。','https://qwenlm.github.io/blog/qwen2.5/')
add('Alibaba Qwen','Qwen3','2025-04','R/C/Z/O','开放权重','Dense + MoE','Thinking/Non-thinking 混合选择与多规模 MoE。','https://qwenlm.github.io/blog/qwen3/')
add('Alibaba Qwen','Qwen3-Next','2025-09','L/E/O','开放权重','混合线性注意力 + MoE','高稀疏 MoE 与混合注意力效率路线。','https://github.com/QwenLM/Qwen3.8')
add('Alibaba Qwen','Qwen3.5','2026-02','V/L/A/R/O','开放权重','Gated DeltaNet + MoE','原生视觉语言；397B-A17B 等、混合注意力。','https://qwen.ai/blog?id=qwen3.5')
add('Alibaba Qwen','Qwen3.6','2026-04','C/R/O','开放权重','混合注意力','2026 年 4 月发布多尺寸系列。','https://github.com/QwenLM/Qwen3.8')
add('Alibaba Qwen','Qwen3.8','2026-08','R/C/A/O','开放权重','混合注意力 + MoE','2.4T-A95B 等：大规模稀疏 MoE 研究路线。','https://github.com/QwenLM/Qwen3.8')
add('DeepSeek','DeepSeek LLM','2024-01','O/Z','开放权重','Dense decoder','DeepSeek 基础系列早期代表。','https://github.com/deepseek-ai/DeepSeek-LLM')
add('DeepSeek','DeepSeek-V2','2024-05','E/C/O','开放权重','MLA + MoE','多头潜在注意力 MLA 与高效 MoE。','https://arxiv.org/abs/2405.04434')
add('DeepSeek','DeepSeek-V3','2024-12','R/C/E/O','开放权重','MLA + MoE','大规模高效预训练与专家路由。','https://api-docs.deepseek.com/updates/')
add('DeepSeek','DeepSeek-R1','2025-01','R/S/O','开放权重','推理强化学习','推理强化学习/蒸馏；R1 属于专项推理分支。','https://github.com/deepseek-ai/DeepSeek-R1')
add('DeepSeek','DeepSeek-V3.1','2025-08','R/C/A','开放权重','MLA + MoE','混合思考模式与 Agent 使用增强。','https://api-docs.deepseek.com/updates/')
add('DeepSeek','DeepSeek-V3.2','2025-12','R/C/A','开放权重','MoE + 推理','推理模式与工具使用演进。','https://api-docs.deepseek.com/updates/')
add('DeepSeek','DeepSeek-V4 Pro / Flash','2026-04','R/C/A/E','API','未公开 / 高效模型','两档新 API，官方于 2026-04-24 上线。','https://api-docs.deepseek.com/updates/')
add('DeepSeek','DeepSeek-V4.1 Flash','2026-09','C/A/E/V','API','未公开','更高效的系列更新；部分视觉版本为实验模型。','https://api-docs.deepseek.com/zh-cn/updates/')
add('Mistral','Mistral 7B','2023-09','E/O','开放权重','Dense decoder','少参数开放 LLM 的里程碑。','https://mistral.ai/news/')
add('Mistral','Mixtral 8x7B','2023-12','O/E','开放权重','MoE','早期高关注度开放 MoE。','https://mistral.ai/news/mixtral-of-experts/')
add('Mistral','Mistral Large','2024-02','R/Z','API','未公开','大型闭源能力路线。','https://mistral.ai/news/')
add('Mistral','Codestral','2024-05','C','受限许可/服务','Dense decoder','面向代码生成与填充。','https://mistral.ai/news/')
add('Mistral','Pixtral 12B','2024-09','V/O','开放权重','VLM','图文视觉语言分支。','https://mistral.ai/news/')
add('Mistral','Devstral','2025-05','C/A/O','开放权重','代码 Agent','面向软件工程任务/Agent。','https://mistral.ai/news/')
add('Mistral','Mistral Large 3','2025-12','O/R/C','开放权重 Apache-2.0','MoE (675B/41B active)','大模型开放权重 MoE；许可宽松。','https://mistral.ai/news/mistral-3/')
add('Mistral','Mistral Small 4','2026-03','E/R/V','开放权重','未详','小模型通用+推理取向。','https://mistral.ai/news/')
add('Google Gemma','Gemma 1','2024-02','O/E','开放权重（Gemma 条款）','Dense decoder','基于 Google Gemini 研究的轻量开放模型家族。','https://blog.google/technology/developers/gemma-open-models/')
add('Google Gemma','Gemma 2','2024-06','O/E','开放权重（Gemma 条款）','Dense decoder','小模型效率与开放权重生态。','https://blog.google/technology/developers/google-gemma-2/')
add('Google Gemma','Gemma 3','2025-03','V/O/E','开放权重（Gemma 条款）','Dense decoder','多模态与端侧部署路线。','https://blog.google/technology/developers/gemma-3/')
add('Google Gemma','Gemma 4','2026-04','R/A/E/V/O','开放权重 Apache-2.0','Dense + MoE','高效本地推理、Agent 与多模态，E2B/4B/26B MoE/31B。','https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/')
add('Google Gemma','Gemma 4 12B','2026-06','V/E/O','开放权重 Apache-2.0','多模态','原生音频输入，笔记本部署定位。','https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/')
add('Moonshot Kimi','Kimi / Moonshot v1','2023-10','Z/L','API','未公开','长上下文助手产品；此处按产品首次公开月份。','https://moonshot.ai',evidence='产品发布月份')
add('Moonshot Kimi','Kimi K2','2025-07','C/A/O','开放权重','MoE','面向代码和工具调用的开放权重系列。','https://github.com/MoonshotAI/Kimi-K2')
add('Moonshot Kimi','Kimi K2 Thinking','2025-11','R/C/A/O','开放权重','MoE','K2 推理增强分支。','https://github.com/MoonshotAI/Kimi-K2')
add('Moonshot Kimi','Kimi K2.5','2026-01','V/C/A/R/O','开放权重','MoE + 视觉','在 K2 Base 上继续预训练图文，视觉 Agent、Agent Swarm。','https://github.com/MoonshotAI/Kimi-K2.5')
add('Z.ai GLM','ChatGLM-6B','2023-03','Z/O/E','开放权重','GLM 架构','中文双语对话开放基础。','https://github.com/THUDM/ChatGLM-6B')
add('Z.ai GLM','GLM-4','2024-01','Z/A','API','未公开','智谱 GLM-4 服务模型系列。','https://github.com/THUDM/GLM-4')
add('Z.ai GLM','GLM-4.5','2025-07','C/R/A/O','开放权重','MoE','Agent/推理/编码融合。','https://github.com/zai-org/GLM-4.5')
add('Z.ai GLM','GLM-5','2026-02','C/A/R/O','开放权重','MoE','面向 Agentic Engineering 的 GLM-5 系列。','https://github.com/zai-org/GLM-5')
add('Z.ai GLM','GLM-5.3 / Flash','2026-08','C/A/E/O/V','开放权重','MoE','开放高端系列 + 原生多模态 Flash。','https://github.com/zai-org/GLM-5')
add('Microsoft Phi','Phi-2','2023-12','E/O','开放权重','Dense decoder','小模型训练数据质量路线。','https://www.microsoft.com/en-us/research/blog/phi-2-the-surprising-power-of-small-language-models/')
add('Microsoft Phi','Phi-3','2024-04','E/O','开放权重','Dense decoder','端侧与高性价比小模型。','https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/')
add('Microsoft Phi','Phi-4','2024-12','E/R/O','开放权重','Dense decoder','合成数据与数据质量增强，14B。','https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/')
add('Microsoft Phi','Phi-4 reasoning','2025-04','E/R/S/O','开放权重','Dense + SFT/RL','14B 复杂推理模型，强数学/科学。','https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/')
add('Ai2 OLMo','OLMo 1','2024-02','O','完全开放（训练配方）','Dense decoder','开放代码、数据、训练过程；研究透明度路线。','https://allenai.org/olmo')
add('Ai2 OLMo','OLMo 2','2024-11','O/R','完全开放（训练配方）','Dense decoder','开放预训练与中间过程的研究平台。','https://allenai.org/olmo')
add('Ai2 OLMo','OLMo 3','2025-11','O/R/S','完全开放（训练配方）','Dense decoder','开放模型流与中间检查点，适合机制研究。','https://allenai.org/blog/olmo3')
add('NVIDIA Nemotron','Nemotron-4 340B','2024-06','O/R','开放权重','Dense decoder','合成数据和模型生态。','https://huggingface.co/nvidia/Nemotron-4-340B-Instruct')
add('NVIDIA Nemotron','Nemotron 3 Super','2026-03','E/A/R/O','开放权重','混合 MoE','120B/12B 激活，高吞吐 Agent 路线。','https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/')
add('NVIDIA Nemotron','Nemotron 3.5 VL/Bolt','2026-10','V/E/A/O','开放权重','混合 MoE','从数据中心到本地 Agent，120B VL/74B/4B 等。','https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/')
# Harness & Evaluation timeline -- distinct entities from models.
H=[]
def harness(n,d,kind,skill,desc,url,origin): H.append(dict(name=n,date=d,kind=kind,skill=skill,desc=desc,url=url,origin=origin))
harness('LangChain','2022-10','开发框架','链式编排','LLM 应用链与工具封装生态。','https://github.com/langchain-ai/langchain','LangChain')
harness('LlamaIndex','2022-11','数据/RAG','检索数据','数据连接与索引/RAG 系统。','https://github.com/run-llama/llama_index','LlamaIndex')
harness('AutoGPT','2023-03','Agent Harness','自治执行','早期自治 Agent 实验系统。','https://github.com/Significant-Gravitas/AutoGPT','社区')
harness('Semantic Kernel','2023-03','开发框架','编排/插件','微软企业级智能体开发编排。','https://github.com/microsoft/semantic-kernel','Microsoft')
harness('AutoGen','2023-09','多Agent','群体协作','多 Agent 通信与协作系统。','https://github.com/microsoft/autogen','Microsoft')
harness('CrewAI','2023-11','多Agent','角色协作','以角色和任务为中心的多 Agent 框架。','https://github.com/crewAIInc/crewAI','CrewAI')
harness('LangGraph','2024-01','开发框架','有状态执行','图/状态机 Agent 工作流。','https://github.com/langchain-ai/langgraph','LangChain')
harness('SWE-agent','2024-04','Agent Harness','代码修复','基准驱动的软件工程代理框架。','https://github.com/SWE-agent/SWE-agent','Princeton')
harness('DSPy','2024-01','开发框架','提示优化','声明式 LLM 程序与优化。','https://github.com/stanfordnlp/dspy','Stanford')
harness('OpenHands','2024-08','Agent Harness','通用软件工程','开放代码执行、文件读写的编码代理。','https://github.com/All-Hands-AI/OpenHands','OpenHands')
harness('Aider','2023-05','Agent Harness','结对编程','终端/仓库级代码协作，repo map。','https://github.com/Aider-AI/aider','社区')
harness('smolagents','2024-12','开发框架','轻量工具调用','短小可扩展的代理工具调用框架。','https://github.com/huggingface/smolagents','Hugging Face')
harness('OpenAI Agents SDK','2025-03','开发框架','执行/追踪','Agent、handoff、guardrail、tracing。','https://github.com/openai/openai-agents-python','OpenAI')
harness('Claude Code','2025-02','Agent Harness','软件工程','终端任务执行、工具使用、仓库与上下文管理。','https://github.com/anthropics/claude-code','Anthropic')
harness('Google ADK','2025-04','开发框架','Agent 构建','Google Agent Development Kit。','https://google.github.io/adk-docs/','Google')
harness('Codex CLI','2025-04','Agent Harness','软件工程','本地沙箱与代码执行代理。','https://github.com/openai/codex','OpenAI')
harness('Gemini CLI','2025-06','Agent Harness','软件工程','开源终端编程代理。','https://github.com/google-gemini/gemini-cli','Google')
harness('mini-SWE-agent','2025-08','Agent Harness','代码修复','极简可重复 Shell-loop 研究基线。','https://github.com/SWE-agent/mini-swe-agent','Princeton')
B=[]
def bench(n,d,kind,desc,url): B.append(dict(name=n,date=d,kind=kind,desc=desc,url=url))
bench('MMLU','2020-09','知识','多学科知识，较易饱和；需要控制污染与提示格式。','https://github.com/hendrycks/test')
bench('HumanEval','2021-07','代码','代码函数生成，Pass@k 需明确采样与执行协议。','https://github.com/openai/human-eval')
bench('GSM8K','2021-10','数学','小学数学文本题，较易饱和。','https://github.com/openai/grade-school-math')
bench('BIG-bench / BBH','2022-06','知识','复杂能力综合测评，任务异质性大。','https://github.com/google/BIG-bench')
bench('HELM','2022-11','评测平台','统一情境中的多指标模型评测。','https://crfm.stanford.edu/helm/')
bench('MT-Bench','2023-06','对话','多轮对话，LLM-as-a-judge 风险。','https://github.com/lm-sys/FastChat')
bench('SWE-bench','2023-10','Agent系统','GitHub issue 修复；Agent/harness 与模型都影响成绩。','https://www.swebench.com/')
bench('GPQA','2023-11','科学','研究生级专业问答。','https://github.com/idavidrein/gpqa')
bench('MMMU','2023-11','多模态','大学级多学科图文理解。','https://mmmu-benchmark.github.io/')
bench('GAIA','2023-11','Agent系统','通用助手真实任务。','https://huggingface.co/gaia-benchmark')
bench('MMLU-Pro','2024-06','知识','更具挑战的多选专家题。','https://github.com/TIGER-AI-Lab/MMLU-Pro')
bench('LiveCodeBench','2024-03','代码','动态时间窗代码能力评测。','https://livecodebench.github.io/')
bench('OSWorld','2024-04','Agent系统','真实 GUI 计算机交互任务。','https://os-world.github.io/')
bench('τ-bench','2024-06','Agent系统','客户服务工具调用长任务与政策遵循。','https://github.com/sierra-research/tau-bench')
bench('BFCL','2024-07','工具调用','函数调用结构和参数正确性。','https://gorilla.cs.berkeley.edu/leaderboard.html')
bench('Humanity’s Last Exam','2025-01','科学','高难专家题；有工具和无工具分开评。','https://lastexam.ai/')
bench('Terminal-Bench','2025-04','Agent系统','终端任务，环境与评测 harness 决定结果。','https://www.tbench.ai/')
bench('BrowseComp','2025-04','Agent系统','深度网络搜索与查证，工具预算敏感。','https://openai.com/index/browsecomp/')
FAMILIES=[
('技术源流','理论与架构','foundation','#798aa2','global'),
('OpenAI','OpenAI · GPT / o','closed','#249ab1','global'),
('Anthropic','Anthropic · Claude','closed','#d08b60','global'),
('Google Gemini','Google · Gemini','closed','#7a83dc','global'),
('Meta Llama','Meta · Llama','open','#548dd1','global'),
('Meta Muse','Meta · Muse','closed','#56aabb','global'),
('Alibaba Qwen','阿里 · Qwen','open','#18a189','china'),
('DeepSeek','DeepSeek','open','#419b91','china'),
('Moonshot Kimi','月之暗面 · Kimi','open','#4091ab','china'),
('Z.ai GLM','智谱 · GLM','open','#478e92','china'),
('Mistral','Mistral','mixed','#b688bc','global'),
('Google Gemma','Google · Gemma','open','#9990d2','global'),
('Microsoft Phi','Microsoft · Phi','open','#c79c64','global'),
('Ai2 OLMo','Ai2 · OLMo','open','#99a374','global'),
('NVIDIA Nemotron','NVIDIA · Nemotron','open','#7ca96a','global')]
D=dict(models=M,harness=H,benchmarks=B,families=[dict(id=i,label=l,kind=k,color=c,region=r) for i,l,k,c,r in FAMILIES],updated='2026-11-13',skills={
'R':['推理 / 数学','#e29a54'],'C':['编程 / 软件工程','#5aa7cb'],'V':['视觉 / 多模态','#ad85d2'],'L':['长上下文 / 记忆','#6997a3'],'E':['效率 / 端侧','#86a76b'],'A':['Agent / 工具','#d27f81'],'Z':['中文 / 多语言','#af9b67'],'O':['权重开放 / 可研究','#78b3a2'],'S':['科学 / STEM','#ac8ea4']})
(ROOT/'data'/'atlas.json').write_text(json.dumps(D,ensure_ascii=False,indent=2),'utf8')
for k,rows in [('models',M),('harness',H),('benchmarks',B)]:
    with (ROOT/'data'/f'{k}.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows({**r,**({'skills':'/'.join(r['skills'])} if 'skills' in r else {})} for r in rows)
print('counts',len(M),len(H),len(B))
(ROOT/'data'/'embedded.js').write_text('const ATLAS_DATA = '+json.dumps(D,ensure_ascii=False,separators=(',',':'))+';','utf8')