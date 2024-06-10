import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Button from "@mui/material/Button";
import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import TextField from "@mui/material/TextField";
import Snackbar from "@mui/material/Snackbar";
import Alert from "@mui/material/Alert";

import axios from "axios";

const lightGray = "#f2f2f2";
const gray = "#cccccc";
const green = "#4caf50";
const white = "#ffffff";

function BooksPage() {
  const [books, setBooks] = useState([]);
  useEffect(() => {
    // Fetch book data from backend API when component mounts
    axios
      .get("http://localhost:5000/books")
      .then((response) => {
        setBooks(response.data);
      })
      .catch((error) => {
        console.error("Error fetching books:", error);
      });
  }, []);

  const [open, setOpen] = useState(false);
  const [newBook, setNewBook] = useState({
    id: "",
    title: "",
    author: "",
    price: "",
  });

  const [editBook, setEditBook] = useState({
    id: "",
    title: "",
    author: "",
    price: "",
  });
  const [editDialogOpen, setEditDialogOpen] = useState(false);

  const [notification, setNotification] = useState({
    open: false,
    message: "",
    severity: "success",
  });

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewBook((prevBook) => ({
      ...prevBook,
      [name]: value,
    }));
  };

  const handleAddBook = () => {
    // Add new book to the books array
    setBooks((prevBooks) => [...prevBooks, newBook]);
    // Close the dialog
    handleClose();
  };

  const handleDeleteBook = (id) => {
    // Filter out the book with the given id
    const updatedBooks = books.filter((book) => book.id !== id);
    setBooks(updatedBooks);
    // Show notification
    setNotification({
      open: true,
      message: "Book deleted successfully!",
      severity: "success",
    });
  };

  const handleEdit = (book) => {
    setEditBook(book);
    setEditDialogOpen(true);
  };

  const handleEditChange = (e) => {
    const { name, value } = e.target;
    setEditBook((prevBook) => ({
      ...prevBook,
      [name]: value,
    }));
  };

  const handleUpdateBook = () => {
    const index = books.findIndex((book) => book.id === editBook.id);
    if (index !== -1) {
      const updatedBooks = [...books];
      updatedBooks[index] = editBook;
      setBooks(updatedBooks);
      setNotification({
        open: true,
        message: "Book updated successfully!",
        severity: "success",
      });
      setEditDialogOpen(false);
    }
  };

  const handleNotificationClose = () => {
    setNotification({ ...notification, open: false });
  };

  return (
    <div
      style={{
        backgroundColor: lightGray,
        padding: "20px",
        margin: "0 auto",
        maxWidth: "1000px",
        overflowY: "auto",
      }}
    >
      <h1 style={{ textAlign: "center" }}>Book List</h1>
      <div style={{ textAlign: "center", marginBottom: "20px" }}>
        <Button variant="contained" color="primary" onClick={handleClickOpen}>
          Add New Book
        </Button>
      </div>
      <Table style={{ border: `1px solid ${gray}` }}>
        <TableHead style={{ backgroundColor: green, color: white }}>
          <TableRow>
            <TableCell
              style={{ border: `1px solid ${gray}`, fontWeight: "bold" }}
            >
              ID
            </TableCell>
            <TableCell
              style={{ border: `1px solid ${gray}`, fontWeight: "bold" }}
            >
              Title
            </TableCell>
            <TableCell
              style={{ border: `1px solid ${gray}`, fontWeight: "bold" }}
            >
              Author
            </TableCell>
            <TableCell
              style={{ border: `1px solid ${gray}`, fontWeight: "bold" }}
            >
              Price
            </TableCell>
            <TableCell
              style={{ border: `1px solid ${gray}`, fontWeight: "bold" }}
            >
              Actions
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {books.map((book) => (
            <TableRow key={book.id}>
              <TableCell style={{ border: `1px solid ${gray}` }}>
                {book.id}
              </TableCell>
              <TableCell style={{ border: `1px solid ${gray}` }}>
                {book.title}
              </TableCell>
              <TableCell style={{ border: `1px solid ${gray}` }}>
                {book.author}
              </TableCell>
              <TableCell style={{ border: `1px solid ${gray}` }}>
                {book.price}
              </TableCell>
              <TableCell style={{ border: `1px solid ${gray}` }}>
                <Button
                  variant="contained"
                  component={Link}
                  to={`/books/${book.id}`}
                  style={{ marginRight: "8px" }}
                >
                  View
                </Button>
                <Button
                  variant="contained"
                  onClick={() => handleEdit(book)}
                  style={{ marginRight: "8px" }}
                >
                  Edit
                </Button>
                <Button
                  variant="contained"
                  onClick={() => handleDeleteBook(book.id)}
                  color="error"
                >
                  Delete
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>Add New Book</DialogTitle>
        <DialogContent>
          <DialogContentText>Please enter book details:</DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            label="ID"
            name="id"
            fullWidth
            value={newBook.id}
            onChange={handleChange}
          />
          <TextField
            margin="dense"
            label="Title"
            name="title"
            fullWidth
            value={newBook.title}
            onChange={handleChange}
          />
          <TextField
            margin="dense"
            label="Author"
            name="author"
            fullWidth
            value={newBook.author}
            onChange={handleChange}
          />
          <TextField
            margin="dense"
            label="Price"
            name="price"
            fullWidth
            value={newBook.price}
            onChange={handleChange}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleAddBook} color="primary">
            Add
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog open={editDialogOpen} onClose={() => setEditDialogOpen(false)}>
        <DialogTitle>Edit Book</DialogTitle>
        <DialogContent>
          <DialogContentText>Please update book details:</DialogContentText>
          <TextField
            autoFocus
            margin="dense"
            label="ID"
            name="id"
            fullWidth
            value={editBook.id}
            onChange={handleEditChange}
          />
          <TextField
            margin="dense"
            label="Title"
            name="title"
            fullWidth
            value={editBook.title}
            onChange={handleEditChange}
          />
          <TextField
            margin="dense"
            label="Author"
            name="author"
            fullWidth
            value={editBook.author}
            onChange={handleEditChange}
          />
          <TextField
            margin="dense"
            label="Price"
            name="price"
            fullWidth
            value={editBook.price}
            onChange={handleEditChange}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditDialogOpen(false)} color="primary">
            Cancel
          </Button>
          <Button onClick={handleUpdateBook} color="primary">
            Update
          </Button>
        </DialogActions>
      </Dialog>

      <Snackbar
        open={notification.open}
        autoHideDuration={3000}
        onClose={handleNotificationClose}
      >
        <Alert
          onClose={handleNotificationClose}
          severity={notification.severity}
        >
          {notification.message}
        </Alert>
      </Snackbar>
    </div>
  );
}

export default BooksPage;
