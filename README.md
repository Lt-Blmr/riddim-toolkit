# Riddim Toolkit

Riddim Toolkit is a MIDI generation system for building reggae, rocksteady, and ska rhythm sections. Define your style, set the key, and let the engine output basslines, skanks, bubble organs, and more using groove logic stored in JSON templates.

## Features
- JSON-based groove templates for core reggae styles
- Style knobs for One Drop, Rockers, Ska, and Steppers
- Modular generation: bass, guitar, organ, clav
- MIDI output for DAWs or iOS apps (AUM, Cubasis)

Jam-ready. Style-flexible. Built for beat nerds and groove lovers alike.

## Project Structure

```text
├── src/              # All source code (main scripts, modules)
├── tests/            # Unit/integration tests, mirrors src/
├── scripts/          # Automation/deployment scripts
├── notebooks/        # Data exploration, analysis (optional)
├── docker/           # Dockerfiles for dev/deploy
├── gcp/              # Cloud configs (optional)
├── rpi/              # Raspberry Pi configs (optional)
├── docs/             # Documentation and guides
├── .pre-commit-config.yaml  # Pre-commit hooks for style/lint
├── .env.example      # Example environment variables
├── pyproject.toml    # Canonical Python config
├── requirements.txt  # Exported requirements for Docker/CI
```

## Developer Workflow

1. Clone repo and create a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Install pre-commit hooks:

   ```bash
   pip install pre-commit
   pre-commit install
   ```

3. Run tests:

   ```bash
   pytest
   ```

4. Format and lint:

   ```bash
   black src tests
   isort src tests
   flake8 src tests
   mypy src
   ```

See `docs/` for full best practices and environment setup.