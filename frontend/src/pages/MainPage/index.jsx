
import { SearchBar } from '../../components/NavBar/layout/SearchBar';

export const MainPage =({mode})=>{
    return(
        <>
        <div className="flex justify-center">
                <SearchBar />
        </div>
        <div className="mt-12 relative flex flex-col items-center">
        {mode}
        
        {/* popular */}
        <div className="mt-9 mb-4 text-3xl">POPULAR</div>
        <div className="h-56 bg-popular-bg rounded-xl shadow-2xl w-4/5 ">
            <div className=" h-1/6 flex justify-start p-3">
                title
            </div>
            <div className="h-4/6 flex justify-center p-3">
                content contentcontentcontentcontentcontent
            </div>
            <div className="h-1/6 flex justify-end pb-3 pr-3">
                author
            </div>
        </div>

        {/* new */}
         <div className="mt-9 mb-4 text-3xl">NEW</div>
        <div className='w-11/12 bg-new-bg h-full pt-5 pb-5 text-center rounded-lg shadow-lg'>
        <div>new contentnew contentnew contentnew contentnew content</div>
        </div>
        <div className='w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg'>
        <div>new contentnew contentnew contentnew contentnew content</div>
        </div>
         <div className='w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg'>
        <div>new contentnew contentnew contentnew contentnew content</div>
        </div>


         {/* recommend */}
       <div className="mt-9 mb-4 text-3xl">RECOMMEND</div>
        <div className='w-11/12 bg-new-bg h-full pt-5 pb-5 text-center rounded-lg shadow-lg'>
        <div>new contentnew contentnew contentnew contentnew content</div>
        </div>
        <div className='w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg'>
        <div>new contentnew contentnew contentnew contentnew content</div>
        </div>
         <div className='w-11/12 bg-new-bg h-full pt-5 pb-5 mt-5 text-center rounded-lg shadow-lg'>
        <div>new contentnew contentnew contentnew contentnew content</div>
        </div>


        </div>
        </>
    );
}