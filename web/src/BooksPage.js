import React, { useState, useEffect } from "react";
import axios from "axios";

function BooksPage() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    // Fetch book data from backend API when component mounts
    axios
      .get("http://api:5000/api/books")
      .then((response) => {
        setBooks(response.data.data.books);
      })
      .catch((error) => {
        console.error("Error fetching books:", error);
      });
  }, []);

  return (
    <div>
      <h1>Books List</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>title</th>
            <th>author</th>
            <th>price</th>
          </tr>
        </thead>
        <tbody>
          {books.map((book) => (
            <tr key={book.id}>
              <td>{book.id}</td>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.price}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default BooksPage;
