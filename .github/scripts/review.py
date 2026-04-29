import os
import anthropic
import requests

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

filepath = os.environ["CHANGED_FILE"]

with open(filepath) as f:
    code = f.read()

message = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": f"""Review this NeetCode/LeetCode solution:

```python
{code}
```

Provide:
1. Edge cases I may have missed
2. Code style / pythonic improvements
3. The canonical approach for this problem type, if mine differs
4. Any improvements you would make to my implementation
5. One key insight to remember for similar problems

Be concise."""
    }]
)

review = message.content[0].text

# Post as a commit comment via GitHub API
comment_body = f"## 🤖 Claude Review: `{filepath}`\n\n{review}"
requests.post(
    f"https://api.github.com/repos/{os.environ['REPO']}/commits/{os.environ['COMMIT_SHA']}/comments",
    headers={
        "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json"
    },
    json={"body": comment_body}
)
print(f"Posted review for {filepath}")
