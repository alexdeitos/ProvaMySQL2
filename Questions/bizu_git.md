IGUALAR ARQUIVO EM BRANCHS DO GIT

### Passos
1. **Certifique-se de estar no branch de destino**:
   Suponha que você editou o arquivo `exemplo.txt` no branch `local` e quer que ele seja igual no branch `main`. Vá para o branch `main`:
   ```bash
   git checkout main
   ```

2. **Copie o arquivo do branch `local`**:
   Use o comando abaixo para trazer o arquivo `exemplo.txt` do branch `local` para o branch `main`:
   ```bash
   git checkout local -- exemplo.txt
   ```
   Isso substitui o `exemplo.txt` no branch `main` pela versão do branch `local`.

3. **Faça o commit da mudança no branch `main`**:
   Após copiar, adicione e confirme a alteração:
   ```bash
   git add exemplo.txt
   git commit -m "Sincronizando exemplo.txt com branch local"
   ```

### Explicação resumida
- O comando `git checkout <branch> -- <arquivo>` copia a versão do arquivo `<arquivo>` do branch `<branch>` para o branch atual, sem alterar outros arquivos.
- Isso evita a necessidade de editar manualmente o mesmo arquivo nos dois branches.
- Se quiser que o arquivo seja idêntico em ambos os branches no futuro, você pode repetir esse processo sempre que alterá-lo em um deles ou considerar usar `git merge` para sincronizar mais arquivos.

### Observação
- Se o arquivo tiver conflitos (edições diferentes em ambos os branches), você pode precisar resolvê-los manualmente após o comando.
- Para o sentido inverso (copiar de `main` para `local`), basta inverter os branches: `git checkout local` e `git checkout main -- exemplo.txt`.


