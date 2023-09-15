# Veno API 
Free API for Jokes, Facts, Questions and more coming soon!

<a href="https://venoapi.vercel.app/">API URL</a>

## API Reference

#### Get Version
Returns the Version and Last Update Date of the API
```http
  GET /api/version
```

#### Get Quote

```http
  GET /api/quote
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `quote` | `string` | Returns a Quote from the API. |

#### Get Song Recommendation

```http
  GET /api/recommendation
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `recommendation` | `string` | Returns a Song Recommendation from the API. |

#### Get Roast

```http
  GET /api/roast/<username>
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `roast/<username>` | `string` | Returns a Joke from the API. |

Required Parameters: `username`

#### Get Joke

```http
  GET /api/joke
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `joke` | `string` | Returns a Joke from the API. |

#### Get Devjoke

```http
  GET /api/devjoke
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `devjoke` | `string` | Returns a programming-related joke from the API. |

#### Get Darkjoke

```http
  GET /api/darkjoke
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `darkjoke` | `string` | Returns a Dark-Joke from the API. |

#### Get Fact

```http
  GET /api/fact
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `fact` | `string` | Returns a Fact from the API. |

#### Get Question

```http
  GET /api/question
```

| Endpoint | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `question` | `string` | Returns a Question from the API. |


## Usage/Examples

```python
import requests

url = requests.get("https://peter-api.up.railway.app/api/darkjoke")
result = url.json()

buildup = result['buildup']
punchline = result['punchline']
joke = buildup + "? " + punchline
print(joke)
```

## Output:
```json
Why did the blind man fall into the well? Because he couldn't see that well.
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
