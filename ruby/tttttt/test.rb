class MyClass < OtherClass
  def create
    @product = MyClass.new(product_params)

    response_to do |_format|
      if @product.save

      end
    end
  end
end
