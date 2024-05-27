import './App.css';
import {Header} from "./components/header";
import {EventList} from "./components/event_list";
import {Route, Routes} from "react-router-dom";
import {EventDetail} from "./components/event_detail";

function App() {
    return (
        <>
            <Header/>
            <Routes>
                <Route path="/" element={<EventList/>}/>
                <Route path="/:id" element={<EventDetail/>}/>
            </Routes>

        </>
    )
}

export default App;
