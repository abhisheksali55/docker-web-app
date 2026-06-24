```mermaid
flowchart LR
    subgraph TOP[""]
        direction LR
        EC2["☁️ Amazon EC2\nCode Server"]
        GH["🐙 GitHub\nCode Push"]
        DOC["🐳 Docker\nContainerize"]
        DC["🐙 Docker Compose\nMulti-container"]
        JEN["⚙️ Jenkins\nCI/CD Engine"]
    end

    subgraph BOT[""]
        direction RL
        WH["🔔 Webhook\nUsers Notified ✅"]
        ACC["🌐 Access\nApplication"]
        CON["🚀 Container\nApp Running"]
        IMG["📦 Build Docker\nImage"]
        SH["💻 Shell Script\nBuild Commands"]
    end

    EC2 --> GH --> DOC --> DC --> JEN
    JEN --> SH
    SH --> IMG --> CON --> ACC --> WH

    style EC2 fill:#FFF3E0,stroke:#FF9900,stroke-width:2px,color:#E65100
    style GH  fill:#F5F5F5,stroke:#333,stroke-width:2px,color:#24292E
    style DOC fill:#E3F2FD,stroke:#0db7ed,stroke-width:2px,color:#0277BD
    style DC  fill:#E3F2FD,stroke:#0db7ed,stroke-width:2px,color:#0277BD
    style JEN fill:#FFEBEE,stroke:#d33833,stroke-width:2px,color:#B71C1C
    style SH  fill:#ECEFF1,stroke:#546E7A,stroke-width:2px,color:#263238
    style IMG fill:#E1F5FE,stroke:#0288d1,stroke-width:2px,color:#01579B
    style CON fill:#E8F5E9,stroke:#2e7d32,stroke-width:2px,color:#1B5E20
    style ACC fill:#F3E5F5,stroke:#7b1fa2,stroke-width:2px,color:#4A148C
    style WH  fill:#EDE7F6,stroke:#6c5ce7,stroke-width:2px,color:#4527A0

    style TOP fill:transparent,stroke:#444,stroke-dasharray:5 5
    style BOT fill:transparent,stroke:#444,stroke-dasharray:5 5
```
