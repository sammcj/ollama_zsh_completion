# Ollama zsh completion plugin for Antidote

The plugin is based on [Obeone's Gist](https://gist.github.com/obeone/9313811fd61a7cbb843e0001a4434c58) 

# installation

With [Antidote](https://github.com/mattmc3/antidote) installation is as simple as editing my `~/.zsh_plugins.txt` file and adding:

```txt
ocodo/ollama_zsh_completion
```

Then reload the shell (I just start a new terminal window) but you can also:

```sh
source ~/.zshrc
```

- - -

## Completion

Command completion for all `ollama` cli commands, [see the original gist for more info](https://gist.github.com/obeone/9313811fd61a7cbb843e0001a4434c58). 

Below is a summary:

```txt
ollama [TAB]
cp      -- Copy a model
create  -- Create a model from a Modelfile
help    -- Help about any command
list    -- List models
pull    -- Pull a model from a registry
push    -- Push a model to a registry
rm      -- Remove a model
run     -- Run a model
serve   -- Start ollama
show    -- Show information for a model
```

```sh
ollama create [TAB] -f [TAB] files...
```

```sh
ollama push|cp|run|rm|show [TAB]
    <list of local models>

# (TODO/FIXME not sure why we'd want this action for pull.)
```

```sh
ollama pull[TAB]
    <list of ollama core models>

Note: https:/ollama.com/library (cached to ~/.cache/ollama_library_models.cache, 1hr TTL)
```

```sh
ollama serve --
--host        -- Specify the host and port
--keep-alive  -- Duration to keep models in memory
--models      -- Path to the models directory
--origins     -- Set allowed origins
```

```sh
ollama help [TAB]
cp      -- Copy a model
create  -- Create a model from a Modelfile
help    -- Help about any command
list    -- List models
pull    -- Pull a model from a registry
push    -- Push a model to a registry
rm      -- Remove a model
run     -- Run a model
serve   -- Start ollama
show    -- Show information for a model
```
