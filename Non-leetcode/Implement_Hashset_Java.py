public class Set<T> {

      private T arrayElement[];

      int size =0;

      public Set(){

            this.arrayElement = null;

      }

      public Set(T[] element){

            arrayElement = element;

            size = arrayElement.length;

      }

      /**

       *add element to set. A check is made to identify whether element is present or not.

       *If not the element can be inserted.

       * @param element

       */

      public void addElement(T element){

            if(!contains(element)){

            if(size == arrayElement.length){

                  incrementArray();

            }

            arrayElement[size++] = element;

            }

      }

     

      /**

       * to check is element is present or not.

       * @param elem

       * @return boolean

       */

      public boolean contains(T elem){

 

            if (elem == null) {

                for (int i = 0; i < size; i++)

                  if (arrayElement[i]==null)

                      return true;

            } else {

                for (int i = 0; i < size; i++)

                  if (elem.equals(arrayElement[i]))

                      return true;

            }

            return false;

         

      }

     

      /**

       * return the size of set.

       * @return int

       */

      public int size(){

            if(arrayElement != null){

                  return arrayElement.length;

            }else

                  return 0;

      }

     

      public void clear(){

            arrayElement = null;

      }

     

      public String toString(){

            if(arrayElement == null  || arrayElement.length ==0 ){

                  return“[EMPTY]”;

            }else{

                  String toStr=”[“;

                  for(int i=0;i<arrayElement.length;i++){

                        toStr+=arrayElement[i]+”,”;

                  }

                  toStr+=”]”;

                  return toStr;

            }

      }

     

      /**

       * to check whether set is empty or not

       * @return

       */

      public boolean isEmpty(){

            if(arrayElement == null || arrayElement.length ==0 )

            return true;

            else

                  return false;

      }

     

      /**

       * this function is used to increment the size of an array

       *

       */

      private void incrementArray(){

            T[] temparray = arrayElement;

            int tempsize=size+5;

             arrayElement =(T[]) new Object[tempsize];

             System.arraycopy(temparray, 0, arrayElement, 0, size);

             

      }

}//Set class ends