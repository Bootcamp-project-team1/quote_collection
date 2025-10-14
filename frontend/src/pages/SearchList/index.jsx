import { Search } from "../../components/Search";
import { useParams } from "react-router-dom";

export const SearchList =()=>{

    // const location = useLocation();
    // const prevInput=location.state?.key;
    const {input} = useParams();

    return(
        <>
        <div className="flex justify-center">
        <Search prevInput={input}/>
        </div>
         <div className="flex mt-10 justify-center">
            " {input} " results
        </div>
        </>
    );
}