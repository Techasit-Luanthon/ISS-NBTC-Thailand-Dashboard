# Techasit Cloudflare Impact Simulator

Educational Python project for safely modeling CDN/WAF/rate-limit behavior.

## Safety boundary

This project is a local simulation. It does not send traffic to Cloudflare,
alter DNS/BGP routes, scan third-party infrastructure, or attempt to disrupt
any external service.

## Run

Python 3.10+ recommended.

```bash
python app.py
```

## Tests

```bash
python -m unittest discover
```

## VS Code

Open this folder in VS Code, select your Python interpreter, then run `app.py`.

## Model

User Traffic → DNS → CDN → WAF → Rate Limiting → Origin

You can extend the simulator with cache-hit ratio, latency, origin health,
regional nodes, and failure scenarios.
