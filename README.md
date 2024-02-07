### How to use the code?
1. Clone the repository
2. Navigate to the directory where the repository is cloned
3. Find the file [colab_web_server.ipynb](./Colab%20Notebook/colab_web_server.ipynb) and open it in Google Colab
4. Run the cells in the notebook then you will get the your `ngrok url`.
5. Copy the `ngrok url`.
6. Now open the directory where the repository is cloned and find the file [ResponseFetcher.py](./ResponseFetcher.py) and open it in any code editor (I am using VSCode).
7. Find the line `url = "http://your_ngrok_url"` and replace `your_ngrok_url` with the `ngrok url` you copied.
8. Save the file and run the file [ResponseFetcher.py](./ResponseFetcher.py) in terminal.
9. Now you can see the response from the server in the terminal.

**Spinnet of the code:**
```python
    fetcher = ColabResponseFetcher("http://your_ngrok_url/recieve_data")
    response = fetcher.fetch("Your message here (any string)")
    print(response)
```
**Developed by: [Vivek Thakur](https://github.com/vivek09thakur)**