### How to use the code?
- [ ] Clone the repo
- [ ] Navigate to the directory where the repo is cloned
- [ ] Find the file [colab_web_server.ipynb](./Colab%20Notebook/colab_web_server.ipynb) and open it in Google Colab
- [ ] Run the cells in the notebook then you will get the your `ngrok url`.
- [ ] Copy the `ngrok url`.
- [ ] Now open the directory where the repo is cloned and find the file [ResponseFetcher.py](./ResponseFetcher.py) and open it in any code editor (I am using VSCode).
- [ ] Find the line `url = "http://your_ngrok_url"` and replace `your_ngrok_url` with the `ngrok url` you copied.
- [ ] Save the file and run the file [ResponseFetcher.py](./ResponseFetcher.py) in terminal.
- [ ] Now you can see the response from the server in the terminal.

**Spinnet of the code:**
```python
    fetcher = ColabResponseFetcher("http://your_ngrok_url/recieve_data")
    response = fetcher.fetch("Your message here (any string)")
    print(response)
```
**Developed by: [Vivek Thakur](https://github.com/vivek09thakur)**
