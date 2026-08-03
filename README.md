
| **Category**   | **Configuration**        | **Example**                   | **Purpose**                                                   | **Required?**             |
| -------------- | ------------------------ | ----------------------------- | ------------------------------------------------------------- | ------------------------- |
| Authentication | `GEMINI_API_KEY`         | `os.getenv("GEMINI_API_KEY")` | Authenticates your application with the Gemini API            | ✅ Yes                     |
| Authentication | `OPENAI_API_KEY`         | `os.getenv("OPENAI_API_KEY")` | Used when connecting to OpenAI                                | Optional                  |
| Model          | `MODEL_NAME`             | `"gemini-2.5-flash-lite"`     | Specifies which AI model to use                               | ✅ Yes                     |
| Model          | `SUMMARY_MODEL`          | `"gemini-2.5-flash-lite"`     | Uses a separate model for summarization                       | Optional                  |
| Model          | `EMBEDDING_MODEL`        | `"text-embedding-004"`        | Converts text into vector embeddings for semantic search      | Optional                  |
| Generation     | `MAX_OUTPUT_TOKENS`      | `800`                         | Maximum length of the AI's generated response                 | Recommended               |
| Generation     | `TEMPERATURE`            | `0.7`                         | Controls creativity vs. determinism                           | Recommended               |
| Generation     | `TOP_P`                  | `0.95`                        | Controls diversity of word selection (nucleus sampling)       | Optional                  |
| Generation     | `TOP_K`                  | `40`                          | Limits the number of candidate tokens considered at each step | Optional                  |
| Conversation   | `MAX_CHAT_HISTORY`       | `20`                          | Maximum number of messages to retain in context               | Recommended               |
| Conversation   | `SYSTEM_PROMPT_FILE`     | `"prompts/system.txt"`        | External file containing the system prompt                    | Optional                  |
| Conversation   | `SUMMARY_AFTER_MESSAGES` | `30`                          | Summarizes older conversations after a threshold              | Optional                  |
| API            | `REQUEST_TIMEOUT`        | `30`                          | Maximum time (seconds) to wait for an API response            | Recommended               |
| API            | `MAX_RETRIES`            | `3`                           | Number of retry attempts after transient failures             | Recommended               |
| Logging        | `LOG_LEVEL`              | `"INFO"`                      | Controls logging verbosity (`DEBUG`, `INFO`, `ERROR`)         | Recommended               |
| Logging        | `LOG_FILE`               | `"chatbot.log"`               | File where application logs are stored                        | Optional                  |
| Application    | `DEBUG`                  | `True`                        | Enables debug mode for development                            | Recommended (Development) |
| Application    | `APP_NAME`               | `"Mental Health Assistant"`   | Application name displayed in logs or UI                      | Optional                  |
| Features       | `ENABLE_SUMMARIES`       | `True`                        | Enables or disables conversation summaries                    | Optional                  |
| Features       | `ENABLE_STREAMING`       | `True`                        | Streams AI responses token by token                           | Optional                  |
| Features       | `ENABLE_MEMORY`          | `False`                       | Enables long-term user memory                                 | Optional                  |
| Database       | `DATABASE_URL`           | `os.getenv("DATABASE_URL")`   | Connection string for the application's database              | Optional                  |
| Database       | `MONGODB_URI`            | `os.getenv("MONGODB_URI")`    | MongoDB connection string                                     | Optional                  |
"""