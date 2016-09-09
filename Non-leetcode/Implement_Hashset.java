 public class HashSet<E> 
	 extends AbstractSet<E> 
	 implements Set<E>, Cloneable, java.io.Serializable 
 { 
	 // 使用 HashMap 的 key 保存 HashSet 中所有元素
	 private transient HashMap<E,Object> map; 
	 // 定义一个虚拟的 Object 对象作为 HashMap 的 value 
	 private static final Object PRESENT = new Object(); 
	 ... 
	 // 初始化 HashSet，底层会初始化一个 HashMap 
	 public HashSet() 
	 { 
		 map = new HashMap<E,Object>(); 
	 } 
	 // 以指定的 initialCapacity、loadFactor 创建 HashSet 
	 // 其实就是以相应的参数创建 HashMap 
	 public HashSet(int initialCapacity, float loadFactor) 
	 { 
		 map = new HashMap<E,Object>(initialCapacity, loadFactor); 
	 } 
	 public HashSet(int initialCapacity) 
	 { 
		 map = new HashMap<E,Object>(initialCapacity); 
	 } 
	 HashSet(int initialCapacity, float loadFactor, boolean dummy) 
	 { 
		 map = new LinkedHashMap<E,Object>(initialCapacity 
			 , loadFactor); 
	 } 
	 // 调用 map 的 keySet 来返回所有的 key 
	 public Iterator<E> iterator() 
	 { 
		 return map.keySet().iterator(); 
	 } 
	 // 调用 HashMap 的 size() 方法返回 Entry 的数量，就得到该 Set 里元素的个数
	 public int size() 
	 { 
		 return map.size(); 
	 } 
	 // 调用 HashMap 的 isEmpty() 判断该 HashSet 是否为空，
	 // 当 HashMap 为空时，对应的 HashSet 也为空
	 public boolean isEmpty() 
	 { 
		 return map.isEmpty(); 
	 } 
	 // 调用 HashMap 的 containsKey 判断是否包含指定 key 
	 //HashSet 的所有元素就是通过 HashMap 的 key 来保存的
	 public boolean contains(Object o) 
	 { 
		 return map.containsKey(o); 
	 } 
	 // 将指定元素放入 HashSet 中，也就是将该元素作为 key 放入 HashMap 
	 public boolean add(E e) 
	 { 
		 return map.put(e, PRESENT) == null; 
	 } 
	 // 调用 HashMap 的 remove 方法删除指定 Entry，也就删除了 HashSet 中对应的元素
	 public boolean remove(Object o) 
	 { 
		 return map.remove(o)==PRESENT; 
	 } 
	 // 调用 Map 的 clear 方法清空所有 Entry，也就清空了 HashSet 中所有元素
	 public void clear() 
	 { 
		 map.clear(); 
	 } 
	 ... 
 } 