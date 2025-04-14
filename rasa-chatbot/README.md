# Rasa Chatbot

This project is a chatbot built using Rasa, an open-source machine learning framework for building conversational AI. The chatbot is designed to understand user intents and respond appropriately based on predefined stories and rules.

## Project Structure

```
rasa-chatbot
├── actions
│   └── actions.py          # Custom action classes for chatbot logic
├── data
│   ├── nlu.yml             # NLU training data for intents and entities
│   ├── stories.yml         # Training stories for conversation flow
│   └── rules.yml           # Rules for structured dialogue management
├── models                   # Directory for storing trained models
├── tests
│   └── test_stories.yml     # Test stories for validating chatbot behavior
├── config.yml               # Configuration settings for the Rasa project
├── credentials.yml          # Credentials for external services
├── domain.yml               # Domain definition including intents, entities, and responses
├── endpoints.yml            # Configuration for Rasa and action server endpoints
└── requirements.txt         # Python dependencies for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd rasa-chatbot
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Train the model**:
   ```
   rasa train
   ```

4. **Run the action server**:
   ```
   rasa run actions
   ```

5. **Run the Rasa server**:
   ```
   rasa run
   ```

## Usage Guidelines

- To interact with the chatbot, you can use the Rasa shell or integrate it with messaging platforms like Slack or Facebook Messenger.
- Modify the `data/nlu.yml`, `data/stories.yml`, and `data/rules.yml` files to customize the chatbot's behavior and responses.
- Use the `tests/test_stories.yml` file to validate the chatbot's responses and ensure it behaves as expected.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.