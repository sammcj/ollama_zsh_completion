# Ollama zsh completion plugin

The plugin is based on [Obeone's Gist](https://gist.github.com/obeone/9313811fd61a7cbb843e0001a4434c58)

# Installation

## With Antidote

I use Antidote for zsh plugins, but if you use a different system for managing your zsh, it's basically the same: just add `ocodo/ollama_zsh_completion` to your plugins list and reload your shell.

With [Antidote](https://github.com/mattmc3/antidote), installation is as simple as editing your `~/.zsh_plugins.txt` file and adding:

```
ocodo/ollama_zsh_completion
```

Then reload:

```sh
source ~/.zshrc
```

Or just start a new shell. Update plugins using `antidote update`.

## With Oh My Zsh

If you use [Oh My Zsh](https://ohmyz.sh/), you can install this plugin manually:

```sh
git clone https://github.com/ocodo/ollama_zsh_completion.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/ollama
```

Then edit your `.zshrc` and add `ollama` to the list of plugins:

```sh
plugins=(... ollama)
```

Reload your shell:

```sh
source ~/.zshrc
```

---

## Completion

Command completion for all `ollama` CLI commands, [see the original gist for more info](https://gist.github.com/obeone/9313811fd61a7cbb843e0001a4434c58).

Examples:

```sh
ollama [TAB]
cp      -- Copy a model
create  -- Create a model from a Modelfile
help    -- Help about any command
list    -- List models
ps      -- List running models
pull    -- Pull a model from a registry
push    -- Push a model to a registry
rm      -- Remove a model
run     -- Run a model
serve   -- Start ollama
show    -- Show information for a model
stop    -- Stop a running model
```

```sh
ollama create -f [TAB]  # File completion for Modelfile
```

```sh
ollama push|cp|run|rm|show [TAB]
# Completion of local models
```

```sh
ollama pull [TAB]
# Completion of models from ollama.com/library

Note: Results cached to ~/.cache/ollama_library_models.cache (1hr TTL)
```

```sh
ollama stop [TAB]
# Completion of running models (via `ollama ps`)
```

```sh
ollama help [TAB]
cp      -- Copy a model
create  -- Create a model from a Modelfile
help    -- Help about any command
list    -- List models
ps      -- List running models
pull    -- Pull a model from a registry
push    -- Push a model to a registry
rm      -- Remove a model
run     -- Run a model
serve   -- Start ollama
show    -- Show information for a model
stop    -- Stop a running model
```
