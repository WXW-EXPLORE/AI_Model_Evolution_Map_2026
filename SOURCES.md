# 来源说明与核查约定

整理时间：**2026-11-13**。这不是未经核实的通用模型排行榜，不展示跨不同实验协议不可比的所谓“综合得分”。

核心数据 `data/atlas.json` 每条模型均包含 `source`、`date`、`architecture`、`access`、`skills`、`summary`，各条官方来源可以点击详情直接查看。

## 主要官网/原始资料

- Transformer：<https://arxiv.org/abs/1706.03762>
- OpenAI GPT-4 / GPT-5 / GPT-6：<https://openai.com/research/index/release/>、<https://openai.com/index/gpt-6-astra/>、<https://openai.com/index/introducing-gpt-5/>
- Anthropic Claude 模型历史：<https://www.anthropic.com/news/models> 与 <https://www.anthropic.com/system-cards>
- Google Gemini：<https://blog.google/products-and-platforms/products/gemini/gemini-3/>、<https://ai.google.dev/gemini-api/docs/changelog>
- Meta Llama 2 / 3 / 4：<https://ai.meta.com/blog/llama-2/>、<https://ai.meta.com/blog/meta-llama-3>、<https://ai.meta.com/blog/llama-4-multimodal-intelligence/>
- Meta Muse：<https://ai.meta.com/research>
- Alibaba Qwen 2.5 / 3 / 3.5 / 3.8：<https://qwenlm.github.io/blog/qwen2.5/>、<https://qwenlm.github.io/blog/qwen3/>、<https://github.com/QwenLM/Qwen3.8>
- DeepSeek：<https://api-docs.deepseek.com/updates/>、<https://github.com/deepseek-ai/DeepSeek-R1>
- Mistral 历史与 Mistral 3：<https://mistral.ai/news/>、<https://mistral.ai/news/mistral-3/>
- Google Gemma 4：<https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/>
- Moonshot Kimi K2.5：<https://github.com/MoonshotAI/Kimi-K2.5>
- GLM-5：<https://github.com/zai-org/GLM-5>
- Microsoft Phi-4：<https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/>
- Ai2 OLMo 3：<https://allenai.org/blog/olmo3>
- NVIDIA Nemotron 3：<https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/>

## 严谨性声明

**模型“血缘”至少有四种**：同品牌/组织系列延续、架构受启发、在前代权重基础上继续训练、蒸馏/教师关系。此地图仅绘制第一种，不把其他三种未经证实地画成实线。

**能力偏好 vs 绝对能力**：某一模型被标为“代码”只是其代表用途或主要设计方向，不能据此推出它在某个固定代码基准上超过其他模型。横向比较性能必须固定评测集版本、模型具体 ID、采样、思考预算、上下文、Harness、工具/API/环境等。

**开放级别**：Open weights 并不自动等同于 OSI 开源，也不说明可访问预训练数据或中间训练权重。研究可复现性必须具体核实。

**日期粒度**：核心模型尽可能以官方新闻或模型卡公开日折算成月份。Harness 与 Benchmark 历史部分一些日期可能是近似首发月份，需在正式发表中再次核实。