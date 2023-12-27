<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Scraped Data Table</title>
    <style>
        #table-container {
            height: 400px; /* Adjust based on your preference */
            overflow-y: scroll;
            border: 1px solid #ccc;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Scraped Data</h1>
    <div id="table-container">
        <table id="data-table">
            <thead>
                <tr>
                    <th>Authors</th>
                    <th>Date</th>
                    <th>Title</th>
                    <th>Publication</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody id="table-body">
                <!-- Data rows will be inserted here by JavaScript -->
            </tbody>
        </table>
    </div>
    <script src="script.js"></script>
    <script>
        // JavaScript to load data from 'data.json' and populate the table
        fetch('https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/data/data.json')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('table-body');
                // Assuming each item in the data is an object with Authors, Date, Title, Publication, and Link
                data.slice(0, 10).forEach(item => {
                    const row = document.createElement('tr');
                    row.innerHTML = `
                        <td>${item.Authors || ''}</td>
                        <td>${item.Date || ''}</td>
                        <td>${item.Title || ''}</td>
                        <td>${item.Publication || ''}</td>
                        <td>${item.Link ? `<a href="${item.Link}" target="_blank">Link</a>` : ''}</td>
                    `;
                    tableBody.appendChild(row);
                });
            })
            .catch(error => {
                console.error('Error fetching data: ', error);
                const tableBody = document.getElementById('table-body');
                const row = document.createElement('tr');
                row.innerHTML = `<td colspan="5">Error loading data.</td>`;
                tableBody.appendChild(row);
            });
    </script>
</body>
</html>
