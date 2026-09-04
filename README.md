# ReqForge

> Build reproducible HTTP requests for API debugging and development.

ReqForge is a small HTTP request builder for composing methods, headers, query parameters, and JSON bodies in a consistent format.

## Highlights

- Build common HTTP methods
- Compose query parameters and headers
- Create JSON request bodies
- Keep request definitions reproducible
- Useful for API debugging and development workflows

## Example

```python
from reqforge import Request

request = Request(
    method="POST",
    url="https://example.com/api",
    headers={"Content-Type": "application/json"},
    json={"message": "hello"},
)

print(request)
```

## Use Cases

- API development
- Request debugging
- Reproducible test cases
- Local tooling and automation

## Design

```text
method + URL
     + headers
     + query
     + body
        ↓
 reproducible request
```

ReqForge is a request-construction utility. It does not bypass authentication or perform exploitation.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
