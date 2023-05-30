import {Route, Routes} from "react-router-dom"
import Layout from "./components/Layout";
import Login from "./components/Login";
import Register from "./components/Register";
import HomePage from "./components/HomePage";


function App() {
  return (
    // <div className='App bg-zinc-500 min-h-screen flex flex-col justify-center items-center'>
    //   <button className="btn btn-primary">App</button>
    // </div>

    <Routes>
      <Route path="/" elementName={<Layout />} >
        <Route path="/" elementName={<HomePage />} />
        <Route path="/login" elementName={<Login />} />
        <Route path="/register" elementName={<Register />} />
      </ Route>
    </Routes>
  );
}

export default App;
