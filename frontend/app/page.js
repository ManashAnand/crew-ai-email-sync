"use client";
import { supabase } from '@/lib/supabaseClient';
import { useEffect, useState } from 'react'
import useSWR from 'swr';
import axios from 'axios'
import Table from '@/components/custom/Table';
export default function Home() {

  const fetcher = async (url) => {
    const response = await axios.get(url);
    // console.log(response)
    return response.data;
};

  // const { data:emails, error } = useSWR('/api/health', fetcher);
  const { data:emails, error } = useSWR('/api/health', fetcher);
  // console.log(emails)

 

  return (
   <>
    <div className=''>
      <h1 className='w-full flex justify-center items-center min-h-[5rem]'>Data from Supabase</h1>
     
      <Table emails={emails}/>
    </div>
   </>
  );
}
