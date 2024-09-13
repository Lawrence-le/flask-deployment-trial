import { useEffect, useState } from "react";
const apiUrl = import.meta.env.VITE_API_URL;

function App() {
  const [messages, setMessages] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const url = `${apiUrl}/api/data`;
    const fetchData = async () => {
      try {
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        setMessages(data.messages); // Handle the messages array
        console.log(data.messages); // Log the messages array for debugging
      } catch (error) {
        setError(error.message); // Set error state
        console.error("Fetch error:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>Messages:</h1>
      <ul>
        {messages.map((message, index) => (
          <li key={index}>{message}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
